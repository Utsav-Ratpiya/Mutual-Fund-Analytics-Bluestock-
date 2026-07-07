# 📊 Mutual Fund Analytics Platform

> **Bluestock Fintech Internship Capstone Project**

An end-to-end Mutual Fund Analytics Platform built using **Python, SQLite, SQL, Jupyter Notebook, and Power BI**. This project analyzes historical mutual fund data, performs financial and risk analytics, and presents interactive business dashboards for investment insights.

---

## 🚀 Project Overview

The objective of this project is to build a complete analytics pipeline for mutual fund data, including:

- Data Ingestion & Validation
- Data Cleaning & Preprocessing
- SQLite Data Warehouse
- SQL Analytics
- Exploratory Data Analysis (EDA)
- Risk & Performance Analytics
- Advanced Financial Metrics
- Interactive Power BI Dashboard
- Business Insights & Reporting

---

## 🎯 Project Objectives

- Build an end-to-end Mutual Fund Analytics Platform
- Analyze historical NAV trends
- Evaluate fund performance using financial metrics
- Study SIP inflows and investor behaviour
- Compare funds with benchmark indices
- Generate dashboard-ready datasets
- Create interactive Power BI reports

---

# 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Programming | Python |
| Database | SQLite, SQL |
| Libraries | Pandas, NumPy, Matplotlib, Plotly, Seaborn, SQLAlchemy, SciPy |
| BI Tool | Power BI |
| Tools | Jupyter Notebook, Git, GitHub |

---

# 📁 Project Structure

```text
Mutual-Fund-Analytics-Bluestock/
│
├── dashboard/
│   │
│   ├── Dashboard images/
│   │   ├── Home.png
│   │   ├── Industry Overview.png
│   │   ├── Fund Performance.png
│   │   ├── Investor Analytics.png
│   │   └── SIP & Market Trend.png
│   │
│   ├── assets/
│   │   ├── icons/
│   │   └── bluestock_logo.png
│   │
│   ├── Dashboard.pdf
│   ├── Dashboard_Theme.json
│   └── bluestock_mf_dashboard.pbix
│
├── data/
│   │
│   ├── raw/
│   │   ├── fund_master.csv
│   │   ├── nav_history.csv
│   │   ├── aum_history.csv
│   │   ├── sip_inflows.csv
│   │   ├── category_inflows.csv
│   │   ├── folio_count.csv
│   │   ├── scheme_performance.csv
│   │   ├── investor_transactions.csv
│   │   ├── portfolio_holdings.csv
│   │   └── benchmark_indices.csv
│   │
│   └── processed/
│       ├── cleaned_nav_history.csv
│       ├── cleaned_transactions.csv
│       ├── cleaned_scheme_performance.csv
│       └── ...
│
├── notebooks/
│   │
│   ├── day1_analysis.ipynb
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports/
│   │
│   ├── charts/
│   │   ├── nav_trend.png
│   │   ├── aum_growth.png
│   │   ├── sip_trend.png
│   │   ├── benchmark_comparison.png
│   │   ├── sharpe_ratio.png
│   │   ├── sortino_ratio.png
│   │   ├── fund_scorecard.png
│   │   ├── max_drawdown.png
│   │   └── rolling_sharpe_chart.png
│   │
│   ├── alpha_beta.csv
│   ├── cagr_comparison.csv
│   ├── fund_scorecard.csv
│   ├── max_drawdown.csv
│   ├── sharpe_ratio.csv
│   ├── sortino_ratio.csv
│   ├── tracking_error.csv
│   ├── var_cvar_report.csv
│   ├── data_dictionary.md
│   ├── data_quality_report.txt
│   ├── day1_observations.txt
│   └── day2_summary.txt
│
├── scripts/
│   │
│   ├── create_database.py
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── database_loader.py
│   ├── verify_database.py
│   ├── validate_amfi_code.py
│   ├── live_nav_fetch.py
│   ├── run_queries.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── bluestock_mf.db
├── requirements.txt
├── LICENSE
└── README.md
```

---

# 📂 Dataset Summary

The project uses **10 financial datasets** covering:

- Fund Master
- NAV History
- Scheme Performance
- Investor Transactions
- Portfolio Holdings
- SIP Inflows
- Category Inflows
- AUM Data
- Benchmark Indices
- Industry Folio Count

---

# 📅 Project Progress

| Module | Status |
|----------|--------|
| Day 1 – Data Ingestion | ✅ Completed |
| Day 2 – Data Cleaning & Database | ✅ Completed |
| Day 3 – Exploratory Data Analysis | ✅ Completed |
| Day 4 – Performance Analytics | ✅ Completed |
| Day 5 – Power BI Dashboard | ✅ Completed |
| Day 6 – Advanced Analytics | 🚧 In Progress |

---

# 📊 Day 1 – Data Ingestion

### Completed

- Project setup
- Imported all datasets
- Data validation
- Live NAV integration
- AMFI code validation
- Initial data quality report

---

# 🧹 Day 2 – Data Cleaning & Database

### Completed

- Cleaned financial datasets
- Removed missing values
- Standardized formats
- Designed SQLite Star Schema

### Database Tables

**Dimension Tables**

- dim_fund
- dim_date

**Fact Tables**

- fact_nav
- fact_transactions
- fact_performance
- fact_aum

---

# 📈 Day 3 – Exploratory Data Analysis

Generated **15+ business visualizations** including:

- NAV Trend Analysis
- AUM Growth
- SIP Trend
- Category Inflow Heatmap
- Investor Demographics
- Geographic Distribution
- Portfolio Sector Allocation
- Correlation Matrix
- Fund Performance Distribution

---

# 📉 Day 4 – Performance Analytics

Calculated key financial metrics:

- Daily Returns
- CAGR (1Y, 3Y, 5Y)
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- Tracking Error
- Composite Fund Scorecard

---

# 📊 Day 5 – Power BI Dashboard

Designed an interactive dashboard consisting of:

### Industry Overview

- Total AUM
- SIP Inflows
- Folio Count
- Industry Trends

### Fund Performance

- Return vs Risk
- Benchmark Comparison
- Fund Ranking
- Scorecard

### Investor Analytics

- State-wise Investments
- Transaction Distribution
- Investor Categories
- SIP Insights

### Dashboard Features

- Interactive Filters
- Drill-down Analysis
- KPI Cards
- Dynamic Charts
- Professional Theme

---

# 📈 Day 6 – Advanced Analytics (In Progress)

Currently implementing advanced financial analytics and investor behavior analysis.

### Planned Tasks

- Historical Value at Risk (VaR 95%)
- Conditional Value at Risk (CVaR)
- Rolling 90-Day Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Fund Recommendation System
- Sector HHI Concentration Analysis
- Advanced Business Insights

### Expected Deliverables

- Advanced_Analytics.ipynb
- var_cvar_report.csv
- recommender.py
- rolling_sharpe_chart.png
---

# 📊 Key Features

- ETL Pipeline
- Data Validation
- Data Cleaning
- SQL Analytics
- SQLite Warehouse
- Financial Risk Metrics
- Performance Evaluation
- Benchmark Comparison
- Investor Analytics
- Portfolio Analytics
- Fund Recommendation
- Interactive Power BI Dashboard
- Business Insights

---

# 📦 Deliverables

### Notebooks

- day1_analysis.ipynb
- EDA_Analysis.ipynb
- Performance_Analytics.ipynb
- Advanced_Analytics.ipynb

### Reports

- Fund Scorecard
- Alpha Beta Report
- Sharpe Ratio
- Sortino Ratio
- Tracking Error
- Maximum Drawdown
- VaR & CVaR Report

### Dashboard

- Power BI (.pbix)
- Dashboard Screenshots
- Interactive Visualizations

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Utsav-Ratpiya/Mutual-Fund-Analytics-Bluestock-.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run data cleaning

```bash
python scripts/data_cleaning.py
```

Create database

```bash
python scripts/create_database.py
```

Load database

```bash
python scripts/database_loader.py
```

---

# 📈 Future Improvements

- Live Mutual Fund API Integration
- Real-time Dashboard Refresh
- Machine Learning Fund Recommendation
- Portfolio Optimization
- Risk Forecasting
- Cloud Deployment
- Streamlit Web Application

---

# 👨‍💻 Author

**Utsav Ratpiya**

B.Tech Computer Science Engineering (AI & ML)

Adani University

Bluestock Fintech Internship

---

## ⭐ If you found this project useful, consider giving it a Star on GitHub!