# 📊 Mutual Fund Analytics Platform

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow?style=for-the-badge&logo=powerbi)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)
![Status](https://img.shields.io/badge/Status-Day%206%20Completed-success?style=for-the-badge)

</p>

---

# 📖 Overview

This project was developed as part of the **Bluestock Fintech Internship Capstone Project**.

The objective of this project is to build a complete **Mutual Fund Analytics Platform** capable of performing end-to-end financial data analytics, beginning with raw dataset ingestion and extending to interactive business intelligence dashboards.

The platform covers every stage of a real-world analytics workflow:

- Data Ingestion
- Data Cleaning & Validation
- Database Design
- SQL Analytics
- Exploratory Data Analysis (EDA)
- Performance Analytics
- Advanced Risk Analytics
- Interactive Power BI Dashboard

The project utilizes **Python, SQL, SQLite, DAX, and Microsoft Power BI** to analyze historical mutual fund data, benchmark indices, investor transactions, portfolio holdings, SIP inflows, risk-adjusted returns, and fund performance.

---

# 🚀 Project Objectives

- Build a complete Mutual Fund Analytics Platform
- Design a scalable SQLite Data Warehouse
- Perform end-to-end ETL pipeline
- Clean and validate financial datasets
- Perform SQL-based financial analytics
- Analyze historical NAV performance
- Study Assets Under Management (AUM) growth
- Analyze SIP inflows across multiple categories
- Perform investor demographic analytics
- Evaluate risk-adjusted mutual fund performance
- Compare funds against benchmark indices
- Generate dashboard-ready datasets
- Build an interactive Power BI dashboard
- Perform advanced portfolio risk analysis
- Generate business insights for investment decision making

---

# 🖥 Dashboard Preview

## 🏠 Home

> dashboard/Dashboard images/Home.png

```markdown
![Home Dashboard](![dashboard/Dashboard%20images/Home.png](https://github.com/Utsav-Ratpiya/Mutual-Fund-Analytics-Bluestock-/blob/main/dashboard/Dashboard%20images/Home.png))
```

---

## 📈 Industry Overview

> dashboard/Dashboard images/Industry Overview.png

```markdown
![Industry Overview](dashboard/Dashboard%20images/Industry%20Overview.png)
```

---

## 📊 Fund Performance

> dashboard/Dashboard images/FundPerformance.png

```markdown
![Fund Performance](dashboard/Dashboard%20images/FundPerformance.png)
```

---

## 👥 Investor Analytics

> dashboard/Dashboard images/InvestorAnalytics.png

```markdown
![Investor Analytics](dashboard/Dashboard%20images/InvestorAnalytics.png)
```

---

## 📉 SIP & Market Trends

> dashboard/Dashboard images/SIP & Market Trend.png

```markdown
![SIP & Market Trends](dashboard/Dashboard%20images/SIP%20%26%20Market%20Trend.png)
```

---

# 🎯 Project Workflow

```
Raw Datasets
      │
      ▼
Data Cleaning
      │
      ▼
Data Validation
      │
      ▼
SQLite Database
      │
      ▼
SQL Analytics
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Performance Analytics
      │
      ▼
Advanced Risk Analytics
      │
      ▼
Power BI Dashboard
      │
      ▼
Business Insights
```

---

# 🛠 Tech Stack

## Programming Language

- Python

---

## Data Analysis

- Pandas
- NumPy
- SciPy

---

## Visualization

- Matplotlib
- Seaborn
- Plotly
- Power BI

---

## Database

- SQLite
- SQLAlchemy
- SQL

---

## Dashboard Development

- Microsoft Power BI
- DAX (Data Analysis Expressions)

---

## Development Tools

- Jupyter Notebook
- VS Code
- Git
- GitHub

---

# 📁 Project Structure

```text
Mutual-Fund-Analytics-Bluestock
│
├── dashboard
│   │
│   ├── Dashboard images
│   │   ├── Home.png
│   │   ├── Industry Overview.png
│   │   ├── FundPerformance.png
│   │   ├── InvestorAnalytics.png
│   │   └── SIP & Market Trend.png
│   │
│   ├── assets
│   │   ├── bluestock_logo.png
│   │   └── icons
│   │
│   ├── Dashboard.pdf
│   ├── Dashboard_Theme.json
│   └── bluestock_mf_dashboard.pbix
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   ├── day1_analysis.ipynb
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports
│   ├── charts
│   ├── alpha_beta.csv
│   ├── cagr_comparison.csv
│   ├── fund_scorecard.csv
│   ├── max_drawdown.csv
│   ├── sharpe_ratio.csv
│   ├── sortino_ratio.csv
│   ├── tracking_error.csv
│   ├── var_cvar_report.csv
│   ├── rolling_sharpe_chart.png
│   ├── data_dictionary.md
│   ├── data_quality_report.txt
│   ├── day1_observations.txt
│   └── day2_summary.txt
│
├── scripts
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
├── sql
│   ├── schema.sql
│   └── queries.sql
│
├── bluestock_mf.db
├── README.md
└── requirements.txt
```

---

# 📂 Datasets Used

The project uses **10 financial datasets** representing different aspects of the Indian Mutual Fund industry.

| Dataset | Description |
|----------|-------------|
| Fund Master | Scheme master information |
| NAV History | Historical daily NAV values |
| AUM by Fund House | Quarterly Assets Under Management |
| Monthly SIP Inflows | Monthly SIP investment inflows |
| Category Inflows | Category-wise net inflows |
| Industry Folio Count | Monthly industry folio statistics |
| Scheme Performance | Risk & performance metrics |
| Investor Transactions | Investor SIP & Lumpsum transactions |
| Portfolio Holdings | Portfolio sector allocation |
| Benchmark Indices | NIFTY 50 & NIFTY 100 benchmark data |

---

# ✅ Day 1 Deliverables

# Project Setup & Data Ingestion

Completed Tasks

- Created complete project structure
- Configured GitHub repository
- Installed all required dependencies
- Imported all mutual fund datasets
- Explored data quality
- Connected Live NAV API
- Implemented AMFI Code Validation
- Generated Initial Data Quality Report

### Files Created

- day1_analysis.ipynb
- data_ingestion.py
- live_nav_fetch.py
- validate_amfi_code.py

---

# ✅ Day 2 Deliverables

# Data Cleaning & Database Design

### Data Cleaning

Completed

- Cleaned NAV History dataset
- Standardized Investor Transactions
- Processed Scheme Performance data
- Removed duplicates
- Filled missing values
- Corrected data types
- Standardized date formats

---

## SQLite Star Schema

### Dimension Tables

- dim_fund
- dim_date

### Fact Tables

- fact_nav
- fact_transactions
- fact_performance
- fact_aum
- fact_sip
- fact_category
- fact_folio
- fact_portfolio

---

## SQL Analytics Performed

- Top Fund Houses by AUM
- Monthly NAV Analysis
- SIP Growth Analysis
- Expense Ratio Analysis
- Fund Performance Ranking
- Category Performance
- State-wise Transactions
- Portfolio Allocation Analysis

---

## Deliverables

- Cleaned CSV Files
- SQLite Database
- SQL Schema
- SQL Queries
- Processed Datasets
- Data Quality Report
- Database Verification Report

---
# ✅ Day 3 Deliverables

# 📊 Exploratory Data Analysis (EDA)

Performed comprehensive exploratory analysis on the cleaned mutual fund datasets to understand industry trends, investor behaviour, fund performance and portfolio composition.

More than **15 business-focused visualizations** were created using **Matplotlib, Seaborn and Plotly**.

---

## 📈 NAV Analysis

Completed

- Daily NAV Trend
- NAV Distribution
- Daily Return Distribution
- NAV Correlation Analysis
- Historical NAV Movement

---

## 💰 AUM Analysis

Completed

- Quarterly AUM Growth
- Top Fund Houses by AUM
- AUM Growth Comparison
- Industry AUM Trend

Key Observation

- SBI Mutual Fund remained the largest AMC throughout the analysis period.

---

## 📊 SIP Analysis

Completed

- Monthly SIP Growth
- SIP Trend Analysis
- SIP Growth Rate

Key Observation

- Highest monthly SIP inflow crossed **₹31,000 Crore**.

---

## 📂 Category Analysis

Completed

- Category-wise Net Inflow
- Monthly Category Heatmap
- Top Performing Categories
- Monthly Category Comparison

---

## 👥 Investor Analytics

Completed

- Investor Age Distribution
- Gender Distribution
- Average SIP by Age Group
- B30 vs T30 Investors
- Income Distribution

---

## 🌍 Geographic Analysis

Completed

- State-wise Transactions
- Top Investment Cities
- Geographic Distribution of Investors

---

## 📑 Folio Analysis

Completed

- Monthly Folio Growth
- Quarterly Folio Growth
- Category-wise Folios

---

## 📉 Performance Analysis

Completed

- Daily Return Distribution
- Return Correlation Matrix
- Return Trend Analysis

---

## 🏦 Portfolio Analysis

Completed

- Sector Allocation
- Top Holdings
- Sector-wise Exposure
- Portfolio Diversification

---

## 📦 Deliverables

- EDA_Analysis.ipynb
- 15+ Analytical Charts
- PNG Chart Exports
- Business Insights
- Dashboard-ready CSV Files

---

# ✅ Day 4 Deliverables

# 📈 Fund Performance Analytics

Performed comprehensive financial performance evaluation using standard mutual fund performance metrics.

---

## 📊 Daily Return Analysis

Completed

- Daily Return Calculation
- Return Validation
- Return Distribution

---

## 📈 CAGR Analysis

Computed

- 1-Year CAGR
- 3-Year CAGR
- 5-Year CAGR
- CAGR Comparison Table

---

## ⚖ Risk Adjusted Performance

Calculated

- Sharpe Ratio
- Sortino Ratio

---

## 📉 Benchmark Analytics

Calculated

- Alpha
- Beta
- Benchmark Comparison
- Tracking Error

---

## 📊 Risk Metrics

Computed

- Maximum Drawdown
- Peak Drawdown Date
- Recovery Analysis

---

## 🏆 Composite Fund Scorecard

Created an overall fund ranking using weighted financial metrics.

### Score Formula

- 30% → 3-Year CAGR
- 25% → Sharpe Ratio
- 20% → Alpha
- 15% → Expense Ratio
- 10% → Maximum Drawdown

---

## 📦 Deliverables

- Performance_Analytics.ipynb
- fund_scorecard.csv
- alpha_beta.csv
- tracking_error.csv
- sharpe_ratio.csv
- sortino_ratio.csv
- max_drawdown.csv
- CAGR Comparison Report
- Benchmark Comparison Charts

---

# ✅ Day 5 Deliverables

# 📊 Interactive Power BI Dashboard

Developed a complete interactive Business Intelligence dashboard using **Microsoft Power BI Desktop**.

The dashboard combines financial analytics, investor analytics, risk metrics and market trends into a professional reporting solution.

---

## Dashboard Features

✔ Multi-page Dashboard

✔ Dynamic Slicers

✔ Interactive Filters

✔ Cross Filtering

✔ Drill-through Navigation

✔ Custom Report Tooltips

✔ DAX Measures

✔ Bluestock Theme

✔ Custom Navigation Sidebar

✔ Professional KPI Cards

✔ Dynamic Benchmark Comparison

✔ Export to PDF

✔ PNG Dashboard Reports

---

# 🏠 Dashboard Pages

## 1️⃣ Home

Provides an overview of the project and dashboard.

Includes

- Dashboard Introduction
- Project Description
- KPI Highlights
- Navigation Panel

---

## 2️⃣ Industry Overview

Provides industry-level insights.

Visuals

- Total AUM KPI
- Total SIP Inflows
- Total Folios
- Total Schemes
- Industry AUM Trend
- AUM by AMC
- Category-wise Net Inflow Distribution

Interactive Filters

- Year
- Fund House

---

## 3️⃣ Fund Performance

Analyzes mutual fund performance.

Visuals

- Risk vs Return Bubble Chart
- NAV vs Benchmark
- Fund Scorecard
- Performance Metrics

Interactive Filters

- Fund House
- Category
- Plan

---

## 4️⃣ Investor Analytics

Analyzes investor behaviour.

Visuals

- Transaction Amount by State
- Transaction Mix
- Monthly Transaction Trend
- Average SIP by Age Group

Interactive Filters

- State
- Age Group
- City Tier

---

## 5️⃣ SIP & Market Trends

Analyzes SIP growth and benchmark movement.

Visuals

- Monthly SIP vs NIFTY50
- Category Heatmap
- Top Categories by Net Inflow

Interactive Filters

- Year
- Category

---

## 6️⃣ Fund NAV Details (Drill-through Page)

Dedicated drill-through report.

Features

- Fund NAV
- Average Return
- Sharpe Ratio
- Alpha
- Beta
- NAV Trend
- NAV vs Benchmark
- Fund Information

---

## 🎯 Interactive Features

Implemented

- Report Page Tooltips
- Drill-through Navigation
- Dynamic DAX Measures
- Responsive Filters
- Cross Highlighting
- Cross Filtering
- Bookmark Navigation
- Custom Sidebar Navigation
- Professional Bluestock Theme

---

# 📸 Dashboard Screenshots

## 🏠 Home

```markdown
![Home](dashboard/Dashboard%20images/Home.png)
```

---

## 📈 Industry Overview

```markdown
![Industry Overview](dashboard/Dashboard%20images/Industry%20Overview.png)
```

---

## 📊 Fund Performance

```markdown
![Fund Performance](dashboard/Dashboard%20images/FundPerformance.png)
```

---

## 👥 Investor Analytics

```markdown
![Investor Analytics](dashboard/Dashboard%20images/InvestorAnalytics.png)
```

---

## 📉 SIP & Market Trends

```markdown
![SIP & Market Trends](dashboard/Dashboard%20images/SIP%20%26%20Market%20Trend.png)
```

---

# 🚀 Key Dashboard Features

- Professional Bluestock UI
- Interactive Sidebar Navigation
- Professional KPI Cards
- Dynamic DAX Measures
- Report Page Tooltips
- Drill-through Analytics
- Custom Theme
- Cross Filtering
- Dynamic Benchmark Comparison
- Professional Business Layout
- Export-ready Dashboard

---

# 📊 Outputs Generated

The project currently generates the following outputs.

## Python Outputs

- Cleaned CSV Files
- SQLite Database
- SQL Reports
- EDA Notebook
- Performance Analytics Notebook
- Fund Scorecard
- Alpha & Beta Report
- Sharpe Ratio Report
- Sortino Ratio Report
- Maximum Drawdown Report
- Tracking Error Report
- Dashboard-ready CSV Files
- Business Insights

---

## Power BI Outputs

- bluestock_mf_dashboard.pbix
- Dashboard.pdf
- Dashboard Theme (.json)
- Dashboard PNG Screenshots
- Interactive Dashboard
- Report Tooltips
- Drill-through Report

---

# ✅ Day 6 Deliverables

# 📊 Advanced Analytics & Risk Metrics

Performed advanced financial analytics and portfolio risk evaluation to enhance investment decision-making capabilities beyond standard performance metrics.

This module focuses on **risk measurement, investor behaviour analysis, portfolio concentration, and intelligent fund recommendation**.

---

## 📉 Historical Value at Risk (VaR)

Calculated **Historical VaR (95%)** for all **40 mutual fund schemes** using the daily return distribution.

### Analysis Performed

- Historical Daily Returns
- 95% Confidence VaR
- Risk Ranking of Funds
- Downside Risk Comparison

### Output

- var_cvar_report.csv

---

## 📉 Conditional Value at Risk (CVaR)

Computed **CVaR (Expected Shortfall)** for every mutual fund.

CVaR estimates the average loss occurring beyond the VaR threshold, providing a more realistic measure of downside risk.

Completed

- Historical CVaR
- Downside Loss Comparison
- Worst-case Risk Analysis

---

## 📈 Rolling 90-Day Sharpe Ratio

Implemented rolling performance analysis using a **90-day moving window**.

Calculated

- Rolling Mean Return
- Rolling Standard Deviation
- Rolling Sharpe Ratio

Visualized performance trends for the **Top 5 Mutual Funds**.

### Output

- rolling_sharpe_chart.png

---

## 👥 Investor Cohort Analysis

Grouped investors according to their **first investment year**.

Computed

- Average SIP Amount
- Total Investment
- Cohort Size
- Most Preferred Mutual Fund
- Investment Growth by Cohort

Generated valuable insights into long-term investor behaviour.

---

## 💳 SIP Continuity Analysis

Analyzed SIP consistency across investors.

Completed

- Average Gap Between SIP Dates
- Investors with 6+ SIP Transactions
- At-risk SIP Detection
- SIP Continuity Rate

### Criteria

Investors having

- Average SIP gap > **35 Days**

were classified as

> **At-Risk Investors**

---

## 🤖 Mutual Fund Recommendation System

Developed a simple rule-based recommendation engine.

### Input

- Low Risk
- Moderate Risk
- High Risk

### Recommendation Logic

Returns the **Top 3 Mutual Funds** based on

- Risk Grade
- Sharpe Ratio
- Overall Performance

### Output

- recommender.py

---

## 📊 Portfolio Concentration Analysis

Calculated **Herfindahl-Hirschman Index (HHI)** for equity mutual funds.

HHI measures portfolio concentration using sector allocation.

Computed

- Sector Weight Distribution
- HHI Score
- Diversification Ranking
- Highly Concentrated Funds
- Highly Diversified Funds

---

## 💡 Business Insights

Prepared **5 advanced business insights** using Jupyter Notebook Markdown.

Examples include

- Highest VaR Funds
- Lowest Risk Funds
- Best Risk-adjusted Performers
- Highest Investing Cohorts
- SIP Continuity Rate
- Most Diversified Funds
- Most Concentrated Portfolios

---

## 📦 Deliverables

- Advanced_Analytics.ipynb
- var_cvar_report.csv
- recommender.py
- rolling_sharpe_chart.png
- Advanced Business Insights

---

# 📈 Current Project Progress

| Day | Module | Status |
|------|---------|--------|
| Day 1 | Project Setup & Data Ingestion | ✅ Completed |
| Day 2 | Data Cleaning & Database Design | ✅ Completed |
| Day 3 | Exploratory Data Analysis (EDA) | ✅ Completed |
| Day 4 | Fund Performance Analytics | ✅ Completed |
| Day 5 | Interactive Power BI Dashboard | ✅ Completed |
| Day 6 | Advanced Analytics & Risk Metrics | ✅ Completed |

---

# 🚀 Overall Project Features

## Data Engineering

- ETL Pipeline
- Data Cleaning
- Data Validation
- SQLite Data Warehouse
- SQL Analytics

---

## Financial Analytics

- NAV Analysis
- AUM Analysis
- SIP Analysis
- Category Analysis
- Portfolio Analysis
- Benchmark Comparison
- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- Tracking Error

---

## Advanced Analytics

- Historical VaR
- Conditional VaR (CVaR)
- Rolling Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Mutual Fund Recommender
- Sector HHI Concentration Analysis
- Advanced Business Insights

---

## Power BI Dashboard

- Home Page
- Industry Overview
- Fund Performance
- Investor Analytics
- SIP & Market Trends
- Fund NAV Drill-through Page

Interactive Features

- Dynamic Filters
- Report Page Tooltips
- Drill-through Navigation
- Dynamic KPI Cards
- Cross Filtering
- Cross Highlighting
- DAX Measures
- Bluestock Theme
- Professional Sidebar Navigation

---

# 📂 Project Outputs

## Data Outputs

- Cleaned CSV Files
- SQLite Database
- SQL Reports
- Data Quality Reports

---

## Analytics Outputs

- EDA Notebook
- Performance Analytics Notebook
- Advanced Analytics Notebook
- Fund Scorecard
- Alpha Beta Report
- Sharpe Ratio Report
- Sortino Ratio Report
- Maximum Drawdown Report
- Tracking Error Report
- VaR & CVaR Report
- Rolling Sharpe Analysis
- Business Insights

---

## Dashboard Outputs

- bluestock_mf_dashboard.pbix
- Dashboard.pdf
- Dashboard Theme (.json)
- Dashboard PNG Screenshots
- Interactive Dashboard
- Report Tooltips
- Drill-through Analytics

---

# ▶️ How to Run

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Utsav-Ratpiya/Mutual-Fund-Analytics-Bluestock-.git
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run Data Cleaning

```bash
python scripts/data_cleaning.py
```

---

## 4️⃣ Create SQLite Database

```bash
python scripts/create_database.py
```

---

## 5️⃣ Load Data into Database

```bash
python scripts/database_loader.py
```

---

## 6️⃣ Verify Database

```bash
python scripts/verify_database.py
```

---

## 7️⃣ Run Jupyter Notebooks

```bash
jupyter notebook
```

Open and execute:

- day1_analysis.ipynb
- EDA_Analysis.ipynb
- Performance_Analytics.ipynb
- Advanced_Analytics.ipynb

---

## 8️⃣ Open Power BI Dashboard

Open

```text
dashboard/bluestock_mf_dashboard.pbix
```

to explore the interactive dashboard.

---

# 🔮 Future Enhancements

Future improvements may include:

- Live Mutual Fund API Integration
- Real-time NAV Updates
- Machine Learning-based Fund Recommendation
- Portfolio Optimization Models
- Predictive NAV Forecasting
- Web Dashboard using Streamlit
- Investor Risk Profiling
- Automated Report Generation
- Cloud Database Integration
- Power BI Service Deployment

---

# 🏆 Project Highlights

- 📊 End-to-End Mutual Fund Analytics Platform
- 🗄 SQLite Data Warehouse
- 📈 15+ Exploratory Data Analysis Visualizations
- 📉 Advanced Financial Performance Analytics
- ⚠ Historical VaR & CVaR Risk Analysis
- 🤖 Mutual Fund Recommendation System
- 📊 Interactive Power BI Dashboard
- 🎯 Drill-through & Custom Tooltips
- 📑 Professional Business Reports
- 💼 Real-world FinTech Analytics Workflow

---

# 👨‍💻 Author

## **Utsav Ratpiya**

**B.Tech Computer Science Engineering (AI & ML)**

Adani University

Bluestock Fintech Internship

Mutual Fund Analytics Capstone Project

---

## ⭐ If you found this project useful, consider giving this repository a Star!

This project demonstrates a complete **end-to-end Mutual Fund Analytics workflow**, covering **Data Engineering, Financial Analytics, Risk Metrics, Advanced Analytics, and Business Intelligence Dashboard Development** using **Python, SQL, SQLite, DAX, and Microsoft Power BI**.