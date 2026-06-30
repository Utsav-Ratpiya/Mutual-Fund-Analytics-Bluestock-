# 📊 Mutual Fund Analytics Platform

## Overview

This project is developed as part of the **Bluestock Fintech Internship Capstone Project**.

The objective is to build a complete **Mutual Fund Analytics Platform** that performs end-to-end mutual fund data analysis, including data ingestion, cleaning, database design, exploratory data analysis (EDA), fund performance analytics, and dashboard-ready reporting.

The project leverages Python, SQL, SQLite, and data visualization libraries to analyze historical NAV, AUM growth, SIP inflows, investor demographics, portfolio holdings, benchmark indices, and risk-adjusted mutual fund performance.

---

# 🎯 Project Objectives

- Build an end-to-end Mutual Fund Analytics Platform
- Perform data ingestion and preprocessing
- Clean and validate financial datasets
- Design a SQLite data warehouse
- Perform SQL-based analytics
- Analyze historical NAV trends
- Study AUM growth and SIP inflows
- Perform Exploratory Data Analysis (EDA)
- Evaluate fund performance using financial metrics
- Compare mutual funds against benchmark indices
- Generate dashboard-ready datasets
- Develop interactive Power BI dashboards

---

# 🛠 Tech Stack

### Programming

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- SQLAlchemy
- SciPy

### Database

- SQLite
- SQL

### Tools

- Jupyter Notebook
- Git
- GitHub
- Power BI (Upcoming)

---

# 📁 Project Structure

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
│   ├── EDA_Analysis.ipynb
│   └── Performance_Analytics.ipynb
│
├── reports/
│   ├── charts/
│   ├── alpha_beta.csv
│   ├── cagr_comparison.csv
│   ├── fund_scorecard.csv
│   ├── max_drawdown.csv
│   ├── sharpe_ratio.csv
│   ├── sortino_ratio.csv
│   ├── tracking_error.csv
│   ├── data_dictionary.md
│   ├── data_quality_report.txt
│   ├── day1_observations.txt
│   └── day2_summary.txt
│
├── scripts/
│   ├── create_database.py
│   ├── data_cleaning.py
│   ├── data_ingestion.py
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

# 📂 Datasets Used

The project utilizes 10 mutual fund datasets.

| Dataset | Description |
|----------|-------------|
| Fund Master | Scheme information |
| NAV History | Daily NAV values |
| AUM by Fund House | Assets Under Management |
| Monthly SIP Inflows | SIP investment data |
| Category Inflows | Category-wise inflows |
| Industry Folio Count | Folio statistics |
| Scheme Performance | Performance metrics |
| Investor Transactions | Investor transaction history |
| Portfolio Holdings | Portfolio allocation |
| Benchmark Indices | NIFTY50 & NIFTY100 |

---

# ✅ Day 1 Deliverables

## Project Setup & Data Ingestion

Completed:

- Created project structure
- Configured GitHub repository
- Installed dependencies
- Imported all datasets
- Explored dataset quality
- Live NAV API integration
- AMFI Code Validation
- Initial Data Quality Report

### Files Created

- day1_analysis.ipynb
- data_ingestion.py
- live_nav_fetch.py
- validate_amfi_code.py

---

# ✅ Day 2 Deliverables

## Data Cleaning

Completed:

- Cleaned NAV History
- Standardized Investor Transactions
- Validated Scheme Performance
- Processed all datasets

## Database Design

Designed SQLite Star Schema.

### Dimension Tables

- dim_fund
- dim_date

### Fact Tables

- fact_nav
- fact_transactions
- fact_performance
- fact_aum

## SQL Analytics

Performed:

- Top Funds by AUM
- Monthly NAV Analysis
- SIP Growth Analysis
- Expense Ratio Analysis
- Fund Performance Ranking
- State-wise Transactions

---

# ✅ Day 3 Deliverables

## Exploratory Data Analysis (EDA)

Generated **15+ analytical visualizations**.

### NAV Analysis

- Daily NAV Trend
- 2023 Bull Run Highlight
- 2024 Market Correction

### AUM Analysis

- AUM Growth
- Top Fund Houses
- SBI Mutual Fund Dominance

### SIP Analysis

- Monthly SIP Trend
- Highest SIP Inflow (₹31,002 Cr)

### Category Analysis

- Monthly Net Inflow Heatmap

### Investor Analytics

- Age Distribution
- Gender Distribution
- Average SIP by Age
- T30 vs B30 Investors

### Geographic Analysis

- State-wise Investments
- Top Cities

### Folio Analysis

- Monthly Growth
- Quarterly Growth
- Category-wise Folios

### Performance Analysis

- Daily Return Distribution
- Correlation Matrix

### Portfolio Analysis

- Sector Allocation
- Top Sector Exposure

### Deliverables

- EDA_Analysis.ipynb
- 15+ Charts
- PNG Exports
- Business Insights

---

# ✅ Day 4 Deliverables

## Fund Performance Analytics

Performed comprehensive mutual fund performance evaluation.

### Daily Return Analysis

- Daily Return Calculation
- Return Distribution Validation

### CAGR Analysis

- 1-Year CAGR
- 3-Year CAGR
- 5-Year CAGR
- CAGR Comparison Table

### Risk Adjusted Performance

- Sharpe Ratio
- Sortino Ratio

### Benchmark Analytics

- Alpha Calculation
- Beta Calculation
- Benchmark Comparison
- Tracking Error

### Risk Analysis

- Maximum Drawdown
- Peak & Bottom Drawdown Dates

### Composite Fund Score

Created a weighted **Fund Score (0–100)** using:

- 30% × 3-Year CAGR Rank
- 25% × Sharpe Ratio Rank
- 20% × Alpha Rank
- 15% × Expense Ratio Rank
- 10% × Maximum Drawdown Rank

### Deliverables

- Performance_Analytics.ipynb
- fund_scorecard.csv
- alpha_beta.csv
- tracking_error.csv
- Benchmark Comparison PNG
- Sharpe Ratio Chart
- Sortino Ratio Chart
- CAGR Chart
- Maximum Drawdown Chart
- Fund Scorecard Chart

---

# 📈 Current Project Progress

| Day | Module | Status |
|------|---------|--------|
| Day 1 | Project Setup & Data Ingestion | ✅ Completed |
| Day 2 | Data Cleaning & Database Design | ✅ Completed |
| Day 3 | Exploratory Data Analysis (EDA) | ✅ Completed |
| Day 4 | Fund Performance Analytics | ✅ Completed |
| Day 5 | Dashboard Development | 🔄 In Progress |

---

# 🚀 Key Features

- Automated ETL Pipeline
- Data Cleaning & Validation
- SQLite Data Warehouse
- SQL Analytics
- Exploratory Data Analysis
- NAV Trend Analysis
- AUM Growth Analysis
- SIP Trend Analysis
- Investor Analytics
- Geographic Analysis
- Portfolio Sector Analysis
- Daily Return Analysis
- CAGR Analysis
- Sharpe Ratio
- Sortino Ratio
- Alpha & Beta
- Maximum Drawdown
- Fund Scorecard
- Benchmark Comparison
- Tracking Error Analysis
- Dashboard-ready CSV Outputs
- Business Insights
- Professional Documentation

---

# ▶️ How to Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Data Cleaning

```bash
python scripts/data_cleaning.py
```

## Create Database

```bash
python scripts/create_database.py
```

## Load Database

```bash
python scripts/database_loader.py
```

## Verify Database

```bash
python scripts/verify_database.py
```

---

# 📊 Outputs

The project generates:

- Cleaned CSV Files
- SQLite Database
- SQL Reports
- EDA Notebook
- Performance Analytics Notebook
- Fund Scorecard
- Alpha & Beta Report
- Tracking Error Report
- Benchmark Comparison Charts
- Business Insights
- Dashboard-ready Datasets
- PNG Charts

---

# 📅 Future Work

Upcoming module:

## Day 5 – Dashboard Development

- Connect Power BI with SQLite
- Industry Overview Dashboard
- Fund Performance Dashboard
- Investor Analytics Dashboard
- SIP & Market Trends Dashboard
- Interactive Filters
- Drill-through Navigation
- Dashboard Export (PBIX)
- Dashboard PDF
- Dashboard PNG Screenshots

---

# 👨‍💻 Author

**Utsav Ratpiya**

B.Tech Computer Science Engineering (AI & ML)

Adani University

Bluestock Fintech Internship

Mutual Fund Analytics Capstone Project