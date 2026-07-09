"""
etl_pipeline.py
================
End-to-end ETL pipeline for the Bluestock Mutual Fund Analytics capstone.

Runs, in order, with no manual steps required:
    1. INGEST   - scan data/raw for source CSVs, log shape/dtypes/nulls
    2. CLEAN    - clean & standardize each dataset, write to data/processed
    3. LOAD     - (re)build the SQLite schema and load all tables
    4. VERIFY   - cross-check row counts between processed CSVs and DB tables

Usage:
    python scripts/etl_pipeline.py
    (works no matter which directory you run it from — all paths are
    resolved relative to this file using pathlib)

Logs are written to both the console and logs/etl_pipeline.log.
"""

import logging
import sys
import time
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text

# ----------------------------------------------------------------------
# PATHS — all resolved relative to this script's location, never hardcoded
# ----------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
DB_PATH = BASE_DIR / "data" / "db" / "bluestock_mf.db"
SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"
LOG_DIR = BASE_DIR / "logs"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------------------
# LOGGING
# ----------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_DIR / "etl_pipeline.log", mode="w"),
    ],
)
log = logging.getLogger("etl_pipeline")


class ETLError(Exception):
    """Raised when a pipeline stage fails in a way that should stop the run."""


# ----------------------------------------------------------------------
# STAGE 1 — INGEST (profile raw files, fail fast if any are missing)
# ----------------------------------------------------------------------
REQUIRED_RAW_FILES = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv",
]


def stage_ingest() -> None:
    log.info("=" * 60)
    log.info("STAGE 1/4: INGEST")
    log.info("=" * 60)

    if not RAW_DIR.exists():
        raise ETLError(f"Raw data directory not found: {RAW_DIR}")

    missing = [f for f in REQUIRED_RAW_FILES if not (RAW_DIR / f).exists()]
    if missing:
        raise ETLError(f"Missing required raw files: {missing}")

    for filename in REQUIRED_RAW_FILES:
        filepath = RAW_DIR / filename
        try:
            df = pd.read_csv(filepath)
        except Exception as exc:
            raise ETLError(f"Failed to read {filename}: {exc}") from exc

        log.info(
            "%-35s shape=%s  nulls=%d  dupes=%d",
            filename,
            df.shape,
            int(df.isnull().sum().sum()),
            int(df.duplicated().sum()),
        )

    log.info("Ingest check complete: all %d raw files readable.", len(REQUIRED_RAW_FILES))


# ----------------------------------------------------------------------
# STAGE 2 — CLEAN
# ----------------------------------------------------------------------
def _clean_nav_history() -> pd.DataFrame:
    df = pd.read_csv(RAW_DIR / "02_nav_history.csv")
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(["amfi_code", "date"]).drop_duplicates()

    # Reindex each fund to a full business-day calendar, then forward-fill,
    # so weekends/holidays don't create gaps or get treated as missing data.
    filled = []
    for amfi_code, fund_df in df.groupby("amfi_code"):
        fund_df = fund_df.set_index("date")
        full_range = pd.date_range(fund_df.index.min(), fund_df.index.max(), freq="B")
        fund_df = fund_df.reindex(full_range)
        fund_df["amfi_code"] = amfi_code
        fund_df["nav"] = fund_df["nav"].ffill()
        fund_df.index.name = "date"
        filled.append(fund_df.reset_index())

    df = pd.concat(filled, ignore_index=True)
    df = df.dropna(subset=["nav"])

    invalid_nav = df[df["nav"] <= 0]
    if len(invalid_nav):
        log.warning("Dropping %d rows with non-positive NAV.", len(invalid_nav))
        df = df[df["nav"] > 0]

    return df


def _clean_investor_transactions() -> pd.DataFrame:
    df = pd.read_csv(RAW_DIR / "08_investor_transactions.csv")
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])

    df["transaction_type"] = df["transaction_type"].astype(str).str.strip().str.title()
    mapping = {"Sip": "SIP", "Lumpsum": "Lumpsum", "Redemption": "Redemption"}
    df["transaction_type"] = df["transaction_type"].replace(mapping)

    before = len(df)
    df = df[df["amount_inr"] > 0]
    if before != len(df):
        log.warning("Dropped %d transactions with non-positive amount_inr.", before - len(df))

    valid_kyc = ["Verified", "Pending", "Rejected"]
    invalid_kyc = df[~df["kyc_status"].isin(valid_kyc)]
    if len(invalid_kyc):
        log.warning("%d transactions have unrecognized kyc_status values.", len(invalid_kyc))

    return df


def _clean_scheme_performance() -> pd.DataFrame:
    df = pd.read_csv(RAW_DIR / "07_scheme_performance.csv")

    numeric_cols = [
        "return_1yr_pct", "return_3yr_pct", "return_5yr_pct",
        "benchmark_3yr_pct", "alpha", "beta", "sharpe_ratio",
        "sortino_ratio", "std_dev_ann_pct", "max_drawdown_pct",
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    invalid_expense = df[(df["expense_ratio_pct"] < 0.1) | (df["expense_ratio_pct"] > 2.5)]
    return_anomalies = df[(df["return_1yr_pct"] > 100) | (df["return_1yr_pct"] < -100)]
    log.info("Expense ratio anomalies flagged: %d", len(invalid_expense))
    log.info("1yr return anomalies flagged: %d", len(return_anomalies))

    return df


def _clean_passthrough(filename: str) -> pd.DataFrame:
    df = pd.read_csv(RAW_DIR / filename)
    return df.drop_duplicates()


CLEANERS = {
    "01_fund_master.csv": lambda: _clean_passthrough("01_fund_master.csv"),
    "02_nav_history.csv": _clean_nav_history,
    "03_aum_by_fund_house.csv": lambda: _clean_passthrough("03_aum_by_fund_house.csv"),
    "04_monthly_sip_inflows.csv": lambda: _clean_passthrough("04_monthly_sip_inflows.csv"),
    "05_category_inflows.csv": lambda: _clean_passthrough("05_category_inflows.csv"),
    "06_industry_folio_count.csv": lambda: _clean_passthrough("06_industry_folio_count.csv"),
    "07_scheme_performance.csv": _clean_scheme_performance,
    "08_investor_transactions.csv": _clean_investor_transactions,
    "09_portfolio_holdings.csv": lambda: _clean_passthrough("09_portfolio_holdings.csv"),
    "10_benchmark_indices.csv": lambda: _clean_passthrough("10_benchmark_indices.csv"),
}


def stage_clean() -> None:
    log.info("=" * 60)
    log.info("STAGE 2/4: CLEAN")
    log.info("=" * 60)

    for raw_name, cleaner in CLEANERS.items():
        out_name = raw_name.replace(".csv", "_cleaned.csv")
        try:
            cleaned = cleaner()
        except Exception as exc:
            raise ETLError(f"Cleaning failed for {raw_name}: {exc}") from exc

        out_path = PROCESSED_DIR / out_name
        cleaned.to_csv(out_path, index=False)
        log.info("%-40s -> %-40s rows=%d", raw_name, out_name, len(cleaned))

    log.info("Clean stage complete.")


# ----------------------------------------------------------------------
# STAGE 3 — LOAD (schema + tables)
# ----------------------------------------------------------------------
TABLE_MAP = {
    "01_fund_master_cleaned.csv": "dim_fund",
    "02_nav_history_cleaned.csv": "fact_nav",
    "03_aum_by_fund_house_cleaned.csv": "fact_aum",
    "07_scheme_performance_cleaned.csv": "fact_performance",
    "08_investor_transactions_cleaned.csv": "fact_transactions",
}

def stage_load() -> None:
    log.info("=" * 60)
    log.info("STAGE 3/4: LOAD")
    log.info("=" * 60)

    if not SCHEMA_PATH.exists():
        raise ETLError(f"Schema file not found: {SCHEMA_PATH}")

    # --------------------------------------------------
    # Remove existing database for a fresh ETL run
    # --------------------------------------------------
    if DB_PATH.exists():
        DB_PATH.unlink()
        log.info("Existing database removed successfully.")

    engine = create_engine(f"sqlite:///{DB_PATH}")

    try:
        with engine.begin() as conn:
            schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")

            statements = [
                stmt.strip()
                for stmt in schema_sql.split(";")
                if stmt.strip()
            ]

            for statement in statements:
                conn.execute(text(statement))

            log.info("Database schema created successfully.")

    except Exception as exc:
        raise ETLError(f"Failed to apply schema: {exc}") from exc

    for csv_name, table_name in TABLE_MAP.items():
        csv_path = PROCESSED_DIR / csv_name
        if not csv_path.exists():
            raise ETLError(f"Expected processed file missing: {csv_path}")
        try:
            df = pd.read_csv(csv_path)
            df.to_sql(table_name, engine, if_exists="replace", index=False)
        except Exception as exc:
            raise ETLError(f"Failed to load {table_name} from {csv_name}: {exc}") from exc
        log.info("%-20s <- %-40s rows=%d", table_name, csv_name, len(df))

    log.info("Load stage complete.")


# ----------------------------------------------------------------------
# STAGE 4 — VERIFY (row-count parity between processed CSVs and DB)
# ----------------------------------------------------------------------
def stage_verify() -> None:
    log.info("=" * 60)
    log.info("STAGE 4/4: VERIFY")
    log.info("=" * 60)

    engine = create_engine(f"sqlite:///{DB_PATH}")
    all_ok = True

    with engine.connect() as conn:
        for csv_name, table_name in TABLE_MAP.items():
            csv_count = len(pd.read_csv(PROCESSED_DIR / csv_name))
            db_count = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}")).scalar()
            status = "MATCH" if csv_count == db_count else "MISMATCH"
            if status == "MISMATCH":
                all_ok = False
            log.info("%-20s CSV=%-8d DB=%-8d %s", table_name, csv_count, db_count, status)

    if not all_ok:
        raise ETLError("Row-count verification failed — see MISMATCH rows above.")

    log.info("Verification complete: all tables match.")


# ----------------------------------------------------------------------
# ENTRY POINT
# ----------------------------------------------------------------------
def main() -> int:
    start_time = time.time()

    log.info("=" * 60)
    log.info("Starting Bluestock Mutual Fund ETL Pipeline")
    log.info("=" * 60)
    log.info("Base directory: %s", BASE_DIR)

    stages = [
        ("ingest", stage_ingest),
        ("clean", stage_clean),
        ("load", stage_load),
        ("verify", stage_verify),
    ]

    for name, func in stages:
        try:
            func()
        except ETLError as exc:
            log.error("Pipeline stopped during '%s' stage: %s", name, exc)
            return 1
        except Exception as exc:  # unexpected errors still get logged, not silently swallowed
            log.exception("Unexpected error during '%s' stage: %s", name, exc)
            return 1

    execution_time = round(time.time() - start_time, 2)

    log.info("=" * 60)
    log.info("ETL PIPELINE COMPLETED SUCCESSFULLY")
    log.info("=" * 60)

    log.info("")
    log.info("ETL PIPELINE SUMMARY")
    log.info("-" * 60)
    log.info("Raw Datasets       : %d", len(REQUIRED_RAW_FILES))
    log.info(
        "Processed Datasets : %d",
        len(list(PROCESSED_DIR.glob("*_cleaned.csv")))
    )
    log.info("Database           : %s", DB_PATH.name)
    log.info("Verification       : PASSED")
    log.info("Execution Time     : %.2f seconds", execution_time)
    log.info("=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())
