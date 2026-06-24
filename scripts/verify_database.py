import pandas as pd
import sqlite3

conn = sqlite3.connect("../bluestock_mf.db")

checks = [

    (
        "../data/processed/01_fund_master_cleaned.csv",
        "dim_fund"
    ),

    (
        "../data/processed/02_nav_history_cleaned.csv",
        "fact_nav"
    ),

    (
        "../data/processed/03_aum_by_fund_house_cleaned.csv",
        "fact_aum"
    ),

    (
        "../data/processed/07_scheme_performance_cleaned.csv",
        "fact_performance"
    ),

    (
        "../data/processed/08_investor_transactions_cleaned.csv",
        "fact_transactions"
    )
]

print("=" * 60)
print("DATABASE VALIDATION")
print("=" * 60)

for csv_file, table in checks:

    csv_count = len(
        pd.read_csv(csv_file)
    )

    db_count = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM {table}",
        conn
    )["cnt"][0]

    status = (
        "MATCH"
        if csv_count == db_count
        else "MISMATCH"
    )

    print(
        f"{table:<20} "
        f"CSV={csv_count:<8} "
        f"DB={db_count:<8} "
        f"{status}"
    )

conn.close()