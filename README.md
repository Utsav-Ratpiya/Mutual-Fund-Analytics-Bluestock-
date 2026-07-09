# 📊 Mutual Fund Analytics Platform

> **Bluestock Fintech Internship Capstone Project**  
> A complete Mutual Fund Analytics platform built using **Python, SQL, and Power BI** to analyze mutual fund performance, investor behavior, portfolio risk, and industry trends.

---

# 📷 Interactive Power BI Dashboard

## 🏠 Industry Overview

![Industry Overview](dashboard/Dashboard%20images/Industry%20Overview.png)

---

## 📊 Fund Performance Dashboard

![Fund Performance](dashboard/Dashboard%20images/Fund%20Performance.png)

---

## 👥 Investor Analytics Dashboard

![Investor Analytics](dashboard/Dashboard%20images/Investor%20Analytics.png)

---

## 📈 SIP And Market Trend Dashboard

![SIP & Market Trend](dashboard/Dashboard%20images/SIP%20&%20Market%20Trend.png)

---

## 🔄 Project Workflow

```text
Raw Datasets
      │
      ▼
Data Ingestion
      │
      ▼
Data Cleaning
      │
      ▼
SQLite Database
      │
      ▼
EDA
      │
      ▼
Performance Analytics
      │
      ▼
Power BI Dashboard
      │
      ▼
Advanced Analytics
      │
      ▼
Recommendation System
```


## 📌 Project Overview

This project analyzes Indian mutual fund data through an end-to-end analytics pipeline, covering:

- Data Cleaning & Preprocessing
- SQL Database Design
- Exploratory Data Analysis (EDA)
- Performance & Risk Analytics
- Power BI Dashboard
- Advanced Analytics
- Mutual Fund Recommendation System

The objective is to transform raw mutual fund datasets into meaningful insights for investors and fund managers.

---

## 🚀 Features

### 📈 Data Analytics
- Cleaned and validated 10 mutual fund datasets
- Exploratory Data Analysis (EDA)
- NAV trend analysis
- AUM growth analysis
- SIP inflow trends
- Category inflow analysis
- Investor demographics
- Portfolio allocation analysis

### 📊 Performance Analytics
- Daily Return Calculation
- CAGR (1Y / 3Y / 5Y)
- Alpha & Beta
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown
- Fund Scorecard
- Benchmark Comparison

### ⚠️ Advanced Risk Analytics
- Historical VaR (95%)
- Conditional VaR (CVaR)
- Rolling 90-Day Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Sector HHI Concentration
- Rule-Based Fund Recommendation System

## 📊 Advanced Analytics

### Rolling 90-Day Sharpe Ratio

![Rolling Sharpe](reports/charts/rolling_sharpe_chart.png)

### Sector HHI Concentration

![Sector HHI](reports/charts/sector_hhi_concentration.png)
---


### 📉 Dashboard (Power BI)
- Industry Overview
- Fund Performance
- Investor Analytics
- SIP & Market Trends
---



## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Libraries | Pandas, NumPy, Matplotlib, Seaborn, Plotly, SQLAlchemy, Requests |
| Database | SQLite |
| Dashboard | Power BI |
| IDE | Jupyter Notebook, VS Code |
| Version Control | Git & GitHub |

---

# 📁 Project Structure

```text
Mutual-Fund-Analytics-Bluestock/
│
├── dashboard/
│   ├── Dashboard images/
│   │   ├── industry_overview.png
│   │   ├── fund_performance.png
│   │   ├── investor_analytics.png
│   │   ├── sip&market_trend.png
│   │   └── home.png
│   │
│   ├── Dashboard.pdf
│   ├── Dashboard_Theme.json
│   └── bluestock_mf_dashboard.pbix
│
│
├── data/
│   │
│   ├── raw/
│   │   ├── 01_fund_master.csv
│   │   ├── ...
│   │   └── 10_benchmark_indices.csv
│   │
│   ├── processed/
│   │    ├── 01_fund_master_cleaned.csv
│   │    ├── ...
│   │    └── 10_benchmark_indices_cleaned.csv
│   │    
│   └── db/
│        └── bluestock_mf.db
│
│
├── notebooks/
│   ├── 01_Data_Ingestion.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_EDA_Analysis.ipynb
│   ├── 04_Performance_Analytics.ipynb
│   └── 05_Advanced_Analytics.ipynb
│
├── logs/
│   └── etl_pipeline.log
│
├── reports/
│   ├── charts/
│   │   ├── rolling_sharpe_chart.png
│   │   ├── sector_hhi_concentration.png
│   │   ├── nav_trend.png
│   │   ├── ...
│   │   └── sip_trend.png
│   │
│   ├── alpha_beta.csv
│   ├── cagr_comparison.csv
│   ├── cohort_analysis.csv
│   ├── fund_scorecard.csv
│   ├── max_drawdown.csv
│   ├── nav_returns.csv
│   ├── rolling_sharpe_summary.csv
│   ├── sector_hhi.csv
│   ├── sharpe_ratio.csv
│   ├── sip_continuity.csv
│   ├── sortino_ratio.csv
│   ├── tracking_error.csv
│   └── var_cvar_report.csv
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── create_database.py
│   ├── data_cleaning.py
│   ├── data_ingestion.py
│   ├── database_loader.py
│   ├── live_nav_fetch.py
│   ├── recommender.py
│   ├── run_queries.py
│   ├── validate_amfi_code.py
│   └── verify_database.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── requirements.txt
├── README.md
└── .gitignore

---

## ⚙️ Automated ETL Pipeline

The project includes a production-style ETL pipeline that automates the complete data workflow.

### Pipeline Stages

```
Raw Data
    ↓
Data Ingestion
    ↓
Data Cleaning
    ↓
SQLite Database Creation
    ↓
Database Validation
    ↓
Analytics & Dashboard
```

### Features

- Automated data ingestion
- Data quality validation
- Data cleaning & preprocessing
- SQLite database generation
- Row count verification
- Logging support
- Error handling


# 📚 Datasets

The project uses **10 cleaned datasets**:

| Dataset |
|----------|
| Fund Master |
| NAV History |
| AUM by Fund House |
| Monthly SIP Inflows |
| Category Inflows |
| Industry Folio Count |
| Scheme Performance |
| Investor Transactions |
| Portfolio Holdings |
| Benchmark Indices |

---

# 📅 Project Progress

## ✅ Day 1
- Project Setup
- Data Loading
- Initial Exploration

## ✅ Day 2
- Data Cleaning
- Missing Value Handling
- SQLite Database Creation

## ✅ Day 3
- Exploratory Data Analysis
- Industry Insights
- Investor Analytics

## ✅ Day 4
- Performance Analytics
- Risk Metrics
- Fund Scorecard

## ✅ Day 5
- Interactive Power BI Dashboard
- KPI Cards
- Investor Dashboard
- Market Trend Dashboard

## ✅ Day 6
- Historical VaR & CVaR
- Rolling Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Sector HHI
- Mutual Fund Recommender

---

# 📊 Reports Generated

- Fund Scorecard
- Alpha & Beta Report
- Sharpe Ratio Report
- Sortino Ratio Report
- CAGR Comparison
- Maximum Drawdown
- Historical VaR & CVaR
- Sector HHI Analysis
- Investor Cohort Analysis
- SIP Continuity Report

---

# 📷 Dashboard Preview

> Dashboard screenshots are available inside:

```text
dashboard/Dashboard images/
```

---

# ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/Utsav-Ratpiya/Mutual-Fund-Analytics-Bluestock.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
cd scripts
python etl_pipeline.py
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

### Open Power BI Dashboard

Open:

```
dashboard/bluestock_mf_dashboard.pbix
```

---

# 🎯 Future Improvements

- Monte Carlo Simulation

- Markowitz Efficient Frontier

- Streamlit Dashboard

- Automated Email Reports

- Scheduled Live NAV Updates

---

# 👨‍💻 Author

**Utsav Ratpiya**

B.Tech CSE (AI & ML)  
Adani University

**Bluestock Fintech Internship – Capstone Project**

---

## ⭐ If you found this project useful, consider giving it a star!