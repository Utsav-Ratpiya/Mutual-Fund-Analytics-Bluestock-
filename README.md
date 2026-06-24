# Mutual Fund Analytics Platform

## Overview

This project is developed as part of the Bluestock Fintech Internship Capstone Project. The objective is to build a Mutual Fund Analytics Platform that performs data ingestion, cleaning, validation, database design, and analytical reporting on mutual fund datasets.

The project uses Python, Pandas, SQLAlchemy, SQLite, and SQL to process and analyze mutual fund data, including NAV history, fund performance, AUM trends, SIP inflows, investor transactions, portfolio holdings, and benchmark indices.

---

## Project Objectives

* Analyze mutual fund performance and growth trends
* Track historical NAV movements
* Study Assets Under Management (AUM)
* Analyze investor transaction patterns
* Build a structured SQLite database for analytics
* Generate insights using SQL queries
* Prepare data for dashboarding and visualization

---

## Tech Stack

* Python
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Matplotlib
* Seaborn
* Plotly
* Jupyter Notebook

---

## Project Structure

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
│
├── reports/
│
├── scripts/
│
├── sql/
│
├── bluestock_mf.db
├── README.md
└── requirements.txt
```

---

## Datasets Used

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

## Day 1 Deliverables

### Project Setup & Data Ingestion

* Created project folder structure
* Configured GitHub repository
* Installed required dependencies
* Loaded and explored all datasets
* Fetched live NAV data using MFAPI
* Validated AMFI codes
* Generated data quality observations

Files Created:

* data_ingestion.py
* live_nav_fetch.py
* validate_amfi_code.py
* day1_analysis.ipynb

---

## Day 2 Deliverables

### Data Cleaning & SQL Database Design

#### Data Cleaning

* Cleaned NAV history dataset
* Standardized investor transactions
* Validated scheme performance metrics
* Generated 10 cleaned datasets

#### Database Design

Implemented SQLite Star Schema:

Dimension Tables:

* dim_fund
* dim_date

Fact Tables:

* fact_nav
* fact_transactions
* fact_performance
* fact_aum

#### Database Loading

* Created SQLite database
* Loaded cleaned datasets using SQLAlchemy
* Verified row counts

#### SQL Analytics

Created analytical SQL queries for:

* Top funds by AUM
* Monthly NAV analysis
* SIP growth trends
* State-wise transactions
* Expense ratio analysis
* Performance ranking

---

## Key Features

* Automated ETL pipeline
* Data validation and quality checks
* SQLite data warehouse design
* Mutual fund performance analytics
* Investor transaction analysis
* SQL-based reporting
* Structured project documentation

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Data Cleaning

```bash
python scripts/data_cleaning.py
```

### Create Database

```bash
python scripts/create_database.py
```

### Load Data into Database

```bash
python scripts/database_loader.py
```

### Verify Database

```bash
python scripts/verify_database.py
```

---

## Author

Utsav Ratpiya

B.Tech Computer Science Engineering (AI & ML)

Adani University

Bluestock Fintech Internship – Mutual Fund Analytics Capstone Project
