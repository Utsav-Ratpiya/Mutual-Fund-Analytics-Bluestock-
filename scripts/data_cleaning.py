import pandas as pd
import os

RAW_PATH = "../data/raw"
PROCESSED_PATH = "../data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

print("=" * 60)
print("STARTING DATA CLEANING")
print("=" * 60)

# =====================================================
# 1. CLEAN NAV HISTORY
# =====================================================

print("\nCleaning 02_nav_history.csv...")

nav_df = pd.read_csv(f"{RAW_PATH}/02_nav_history.csv")

# Parse dates
nav_df["date"] = pd.to_datetime(nav_df["date"])

# Sort by AMFI code and date
nav_df = nav_df.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
nav_df = nav_df.drop_duplicates()

# Forward-fill missing NAV values
nav_df["nav"] = (
    nav_df.groupby("amfi_code")["nav"]
    .ffill()
)

# Validate NAV > 0
invalid_nav = nav_df[
    nav_df["nav"] <= 0
]

print(f"Invalid NAV records: {len(invalid_nav)}")
print(f"Rows saved: {len(nav_df)}")

nav_df.to_csv(
    f"{PROCESSED_PATH}/02_nav_history_cleaned.csv",
    index=False
)

print("02_nav_history_cleaned.csv ✓")


# =====================================================
# 2. CLEAN INVESTOR TRANSACTIONS
# =====================================================

print("\nCleaning 08_investor_transactions.csv...")

txn_df = pd.read_csv(
    f"{RAW_PATH}/08_investor_transactions.csv"
)

# Fix date formats
txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"]
)

# Standardize transaction types
txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .replace(mapping)
)

# Validate amount > 0
txn_df = txn_df[
    txn_df["amount_inr"] > 0
]

# Validate KYC values
valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

invalid_kyc = txn_df[
    ~txn_df["kyc_status"].isin(valid_kyc)
]

print(f"Invalid KYC records: {len(invalid_kyc)}")
print(f"Rows saved: {len(txn_df)}")

txn_df.to_csv(
    f"{PROCESSED_PATH}/08_investor_transactions_cleaned.csv",
    index=False
)

print("08_investor_transactions_cleaned.csv ✓")


# =====================================================
# 3. CLEAN SCHEME PERFORMANCE
# =====================================================

print("\nCleaning 07_scheme_performance.csv...")

perf_df = pd.read_csv(
    f"{RAW_PATH}/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct"
]

# Convert return columns to numeric
for col in return_cols:
    perf_df[col] = pd.to_numeric(
        perf_df[col],
        errors="coerce"
    )

# Expense ratio validation
invalid_expense = perf_df[
    (perf_df["expense_ratio_pct"] < 0.1)
    |
    (perf_df["expense_ratio_pct"] > 2.5)
]

# Return anomaly detection
return_anomalies = perf_df[
    (perf_df["return_1yr_pct"] > 100)
    |
    (perf_df["return_1yr_pct"] < -100)
]

print(
    f"Expense ratio anomalies: {len(invalid_expense)}"
)

print(
    f"Return anomalies: {len(return_anomalies)}"
)

print(f"Rows saved: {len(perf_df)}")

perf_df.to_csv(
    f"{PROCESSED_PATH}/07_scheme_performance_cleaned.csv",
    index=False
)

print("07_scheme_performance_cleaned.csv ✓")


# =====================================================
# 4. CLEAN REMAINING DATASETS
# =====================================================

print("\nCleaning remaining datasets...")

other_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in other_files:

    df = pd.read_csv(
        f"{RAW_PATH}/{file}"
    )

    # Remove duplicates
    df = df.drop_duplicates()

    cleaned_name = file.replace(
        ".csv",
        "_cleaned.csv"
    )

    df.to_csv(
        f"{PROCESSED_PATH}/{cleaned_name}",
        index=False
    )

    print(f"{cleaned_name} ✓")


# =====================================================
# SUMMARY
# =====================================================

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nGenerated Files:")

for file in sorted(os.listdir(PROCESSED_PATH)):
    print(f"✓ {file}")