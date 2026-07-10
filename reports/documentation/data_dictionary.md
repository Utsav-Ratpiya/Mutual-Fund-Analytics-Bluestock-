# 📖 Mutual Fund Analytics Data Dictionary

This document describes the datasets used in the **Mutual Fund Analytics Platform** developed during the Bluestock Fintech Internship.

---

# Dataset 01 – Fund Master

**Source:** `01_fund_master.csv`

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Unique AMFI scheme identifier |
| scheme_name | Text | Name of the mutual fund scheme |
| fund_house | Text | Asset Management Company (AMC) |
| category | Text | Mutual fund category |
| sub_category | Text | Mutual fund sub-category |
| plan | Text | Direct or Regular plan |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Annual expense ratio (%) |
| exit_load_pct | Float | Exit load percentage (%) |
| risk_category | Text | Risk classification |

---

# Dataset 02 – NAV History

**Source:** `02_nav_history.csv`

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Mutual fund identifier |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

# Dataset 03 – AUM by Fund House

**Source:** `03_aum_by_fund_house.csv`

**Description**

Contains Assets Under Management (AUM) statistics for Asset Management Companies.

### Important Fields

- Fund House
- Quarter
- AUM (₹ Crore)
- Number of Schemes

---

# Dataset 04 – Monthly SIP Inflows

**Source:** `04_monthly_sip_inflows.csv`

**Description**

Contains monthly Systematic Investment Plan (SIP) investment statistics.

### Important Fields

- Month
- SIP Amount (₹ Crore)
- New SIP Accounts
- SIP Growth (%)

---

# Dataset 05 – Category Inflows

**Source:** `05_category_inflows.csv`

**Description**

Contains category-wise net inflow information across different mutual fund categories.

### Important Fields

- Category
- Month
- Net Inflow (₹ Crore)

---

# Dataset 06 – Industry Folio Count

**Source:** `06_industry_folio_count.csv`

**Description**

Contains industry-wide folio statistics used for investor growth analysis.

### Important Fields

- Month
- Equity Folios
- Hybrid Folios
- Other Folios
- Total Folios

---

# Dataset 07 – Scheme Performance

**Source:** `07_scheme_performance.csv`

**Description**

Contains historical return and performance information for mutual fund schemes.

### Important Fields

- AMFI Code
- Scheme Name
- 1-Year Return
- 3-Year Return
- 5-Year Return
- Benchmark Return
- CAGR

---

# Dataset 08 – Investor Transactions

**Source:** `08_investor_transactions.csv`

**Description**

Contains investor transaction records used for behavioral and demographic analysis.

### Important Fields

- Investor ID
- AMFI Code
- Transaction Type
- Transaction Amount
- State
- Age Group
- Gender

---

# Dataset 09 – Portfolio Holdings

**Source:** `09_portfolio_holdings.csv`

**Description**

Contains portfolio allocation and sector holdings for mutual fund schemes.

### Important Fields

- AMFI Code
- Stock Name
- Sector
- Market Value
- Portfolio Weight (%)

---

# Dataset 10 – Benchmark Indices

**Source:** `10_benchmark_indices.csv`

**Description**

Contains benchmark index values used for performance comparison.

### Important Fields

- Date
- Index Name
- Index Value

---

# Data Processing Summary

The Mutual Fund Analytics Platform utilizes **10 primary datasets** covering fund information, NAV history, AUM, SIP inflows, category inflows, investor transactions, portfolio holdings, benchmark indices, and scheme performance.

These datasets are processed through a Python-based **ETL pipeline**, where the data is:

- Extracted from raw CSV files
- Cleaned and standardized
- Validated for data quality and consistency
- Loaded into a SQLite database
- Used for SQL analysis, exploratory data analysis (EDA), performance analytics, advanced analytics, portfolio optimization, Monte Carlo simulation, and interactive Power BI dashboard development.

---

# Data Sources

- AMFI India (Association of Mutual Funds in India)
- MFAPI (Mutual Fund API)
- Public Mutual Fund Datasets
- Benchmark Index Data (Nifty/BSE)

---

# Project Repository

GitHub Repository:

**https://github.com/Utsav-Ratpiya/Mutual-Fund-Analytics-Bluestock-**