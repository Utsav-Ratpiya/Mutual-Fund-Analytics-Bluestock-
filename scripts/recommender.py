# ============================================================
# Mutual Fund Recommendation System
# Bluestock Fintech Internship
# Author : Utsav Ratpiya
# ============================================================

import pandas as pd

# ============================================================
# Load Dataset
# ============================================================

funds = pd.read_csv(
    "../data/processed/07_scheme_performance_cleaned.csv"
)

# ============================================================
# Display Header
# ============================================================

print("\n" + "=" * 90)
print("        MUTUAL FUND RECOMMENDATION SYSTEM")
print("=" * 90)

print("\nAvailable Risk Appetites")
print("-------------------------")
print("1. Low")
print("2. Moderate")
print("3. High")

# ============================================================
# User Input
# ============================================================

choice = input(
    "\nEnter Risk Appetite (Low / Moderate / High): "
).strip().title()

# ============================================================
# Risk Mapping
# ============================================================

risk_mapping = {
    "Low": ["Low"],
    "Moderate": ["Moderate", "Moderately High"],
    "High": ["High", "Very High"]
}

if choice not in risk_mapping:
    print("\n❌ Invalid Risk Appetite!")
    print("Please choose only Low, Moderate or High.")
    exit()

# ============================================================
# Filter Recommended Funds
# ============================================================

recommended = funds[
    funds["risk_grade"].isin(
        risk_mapping[choice]
    )
].copy()

recommended = recommended.sort_values(
    by="sharpe_ratio",
    ascending=False
)

top3 = recommended.head(3).copy()

# ============================================================
# Format Table
# ============================================================

display_table = top3[
    [
        "scheme_name",
        "fund_house",
        "risk_grade",
        "sharpe_ratio",
        "expense_ratio_pct",
        "return_3yr_pct"
    ]
].copy()

display_table.columns = [
    "Scheme Name",
    "Fund House",
    "Risk Grade",
    "Sharpe",
    "Expense %",
    "3Y Return %"
]

display_table["Sharpe"] = display_table["Sharpe"].round(2)
display_table["Expense %"] = display_table["Expense %"].round(2)
display_table["3Y Return %"] = display_table["3Y Return %"].round(2)

display_table.index = [
    "1",
    "2",
    "3"
]

# ============================================================
# Display Recommendation
# ============================================================

print("\n" + "=" * 90)
print(f" Top 3 Recommended Funds ({choice} Risk Appetite)")
print("=" * 90)

print(display_table.to_string())

print("=" * 90)

print("\nRecommendation Summary")
print("-----------------------")

best = display_table.iloc[0]

print(f"Best Recommended Fund : {best['Scheme Name']}")
print(f"Fund House           : {best['Fund House']}")
print(f"Sharpe Ratio         : {best['Sharpe']}")
print(f"Risk Grade           : {best['Risk Grade']}")

print("\nNote:")
print("Recommendations are based on historical Sharpe Ratio")
print("within the selected risk category and should not be")
print("considered as financial advice.")

print("\n" + "=" * 90)
print("Recommendation Generated Successfully")
print("=" * 90)