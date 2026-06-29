# Mutual Fund Analytics Platform

## Overview

This project is developed as part of the **Bluestock Fintech Internship Capstone Project**. The objective is to build a Mutual Fund Analytics Platform that performs data ingestion, cleaning, validation, database design, exploratory data analysis (EDA), and performance analytics on mutual fund datasets.

The platform uses Python, Pandas, SQLAlchemy, SQLite, SQL, Plotly, and Seaborn to analyze historical NAV, AUM growth, SIP inflows, investor behavior, portfolio holdings, and benchmark indices.

---

# Project Objectives

- Analyze mutual fund performance and growth trends
- Track historical NAV movements
- Study Assets Under Management (AUM)
- Analyze SIP inflows and investor transactions
- Build a structured SQLite data warehouse
- Generate insights using SQL and Python
- Perform Exploratory Data Analysis (EDA)
- Prepare datasets for dashboards and business reporting

---

# Tech Stack

- Python
- Pandas
- NumPy
- SQLAlchemy
- SQLite
- SQL
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook

---

# Project Structure

```text
Capstone Mutual Fund Analytics
│
├── dashboard/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── day1_analysis.ipynb
│   └── EDA_Analysis.ipynb
│
├── reports/
│   ├── charts/
│   ├── data_dictionary.md
│   ├── data_quality_report.txt
│   ├── day1_observations.txt
│   └── day2_summary.txt
│
├── scripts/
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── create_database.py
│   ├── database_loader.py
│   ├── live_nav_fetch.py
│   ├── run_queries.py
│   ├── validate_amfi_code.py
│   └── verify_database.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── bluestock_mf.db
├── README.md
└── requirements.txt
```

---

# Datasets Used

The project uses the following datasets:

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

# Day 1 Deliverables

## Project Setup & Data Ingestion

Completed:

- Created project folder structure
- Configured GitHub repository
- Installed required dependencies
- Loaded all datasets into Pandas
- Explored data structure and quality
- Fetched live NAV using MFAPI
- Validated AMFI scheme codes
- Generated initial data quality observations

### Files Created

- data_ingestion.py
- live_nav_fetch.py
- validate_amfi_code.py
- day1_analysis.ipynb

---

# Day 2 Deliverables

## Data Cleaning

Completed:

- Cleaned NAV history dataset
- Standardized investor transaction data
- Validated scheme performance metrics
- Cleaned all project datasets
- Generated processed CSV files

## Database Design

Designed a SQLite Star Schema.

### Dimension Tables

- dim_fund
- dim_date

### Fact Tables

- fact_nav
- fact_transactions
- fact_performance
- fact_aum

## Database Loading

Completed:

- Created SQLite database
- Loaded cleaned datasets using SQLAlchemy
- Verified table row counts

## SQL Analytics

Implemented analytical SQL queries for:

- Top funds by AUM
- Monthly NAV analysis
- SIP growth trends
- State-wise transactions
- Expense ratio analysis
- Performance ranking

---

# Day 3 Deliverables

## Exploratory Data Analysis (EDA)

Performed detailed exploratory analysis using the processed datasets and generated **15+ analytical charts**.

### NAV Analysis

- Daily NAV Trend (2022–2026)
- Highlighted 2023 Bull Run
- Highlighted 2024 Market Correction

### AUM Analysis

- Fund House AUM Growth (2022–2025)
- SBI Mutual Fund dominance (~₹12.5 Lakh Crore)
- Top 10 Fund Houses by AUM

### SIP Analysis

- Monthly SIP Inflow Trend
- Annotated all-time high SIP inflow (₹31,002 Cr)

### Category Analysis

- Category-wise Monthly Net Inflow Heatmap

### Investor Demographics

- Age Group Distribution
- Gender Distribution
- SIP Amount by Age Group
- T30 vs B30 Investor Distribution

### Geographic Analysis

- State-wise SIP Investment
- Top 10 Cities by SIP Investment

### Folio Analysis

- Industry Folio Growth
- Category-wise Folio Growth
- Monthly Folio Count Increase
- Quarterly Average Folio Count

### Performance Analysis

- Daily NAV Return Distribution
- NAV Return Correlation Matrix (Top 10 Funds)

### Portfolio Analysis

- Sector Allocation Donut Chart
- Top 10 Sectors by Portfolio Weight

### Deliverables

Created:

- EDA_Analysis.ipynb
- 15+ Visualization Charts
- Exported PNG Charts
- Documented 10 Key EDA Findings

---

# Current Project Progress

| Day | Module | Status |
|------|---------|--------|
| Day 1 | Project Setup & Data Ingestion | ✅ Completed |
| Day 2 | Data Cleaning & Database Design | ✅ Completed |
| Day 3 | Exploratory Data Analysis (EDA) | ✅ Completed |
| Day 4 | Fund Performance Analytics | 🔄 In Progress |

---

# Key Features

- Automated ETL Pipeline
- Data Cleaning & Validation
- SQLite Data Warehouse
- SQL-based Analytics
- Exploratory Data Analysis
- Interactive Plotly Visualizations
- NAV Trend Analysis
- AUM Growth Analysis
- SIP Trend Analysis
- Investor Demographic Analysis
- Geographic Investment Analysis
- Portfolio Sector Allocation
- Correlation Analysis
- Business Insight Generation
- Structured Documentation

---

# How to Run

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Run Data Cleaning

```bash
python scripts/data_cleaning.py
```

## 3. Create Database

```bash
python scripts/create_database.py
```

## 4. Load Data into Database

```bash
python scripts/database_loader.py
```

## 5. Verify Database

```bash
python scripts/verify_database.py
```

---

# Outputs

The project generates:

- Cleaned datasets
- SQLite Database
- SQL Analytics
- EDA Notebook
- PNG Charts
- Business Insights
- Data Quality Reports

---

# Future Work

The next phase includes:

- Daily Return Calculation
- CAGR (1Y, 3Y, 5Y)
- Sharpe Ratio
- Sortino Ratio
- Alpha & Beta
- Maximum Drawdown
- Fund Scorecard (0–100)
- Benchmark Comparison
- Tracking Error Analysis
- Interactive Dashboard

---

# Author

**Utsav Ratpiya**

B.Tech Computer Science Engineering (AI & ML)

Adani University

Bluestock Fintech Internship – Mutual Fund Analytics Capstone Project