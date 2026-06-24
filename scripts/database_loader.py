import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///../bluestock_mf.db"
)

print("=" * 50)
print("LOADING DATABASE")
print("=" * 50)

# --------------------------
# dim_fund
# --------------------------

fund_df = pd.read_csv(
    "../data/processed/01_fund_master_cleaned.csv"
)

fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"dim_fund loaded ({len(fund_df)} rows)"
)

# --------------------------
# fact_nav
# --------------------------

nav_df = pd.read_csv(
    "../data/processed/02_nav_history_cleaned.csv"
)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"fact_nav loaded ({len(nav_df)} rows)"
)

# --------------------------
# fact_transactions
# --------------------------

txn_df = pd.read_csv(
    "../data/processed/08_investor_transactions_cleaned.csv"
)

txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"fact_transactions loaded ({len(txn_df)} rows)"
)

# --------------------------
# fact_performance
# --------------------------

perf_df = pd.read_csv(
    "../data/processed/07_scheme_performance_cleaned.csv"
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"fact_performance loaded ({len(perf_df)} rows)"
)

# --------------------------
# fact_aum
# --------------------------

aum_df = pd.read_csv(
    "../data/processed/03_aum_by_fund_house_cleaned.csv"
)

aum_df.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"fact_aum loaded ({len(aum_df)} rows)"
)

print("\nDatabase loaded successfully.")