# Mutual Fund Analytics Data Dictionary

## Dataset 01 - Fund Master

Source: 01_fund_master.csv

| Column            | Data Type | Description                   |
| ----------------- | --------- | ----------------------------- |
| amfi_code         | Integer   | Unique AMFI scheme identifier |
| scheme_name       | Text      | Name of mutual fund scheme    |
| fund_house        | Text      | Asset Management Company      |
| category          | Text      | Fund category                 |
| sub_category      | Text      | Fund sub-category             |
| plan              | Text      | Direct/Regular plan           |
| benchmark         | Text      | Benchmark index               |
| expense_ratio_pct | Float     | Annual expense ratio          |
| exit_load_pct     | Float     | Exit load percentage          |
| risk_category     | Text      | Risk classification           |

---

## Dataset 02 - NAV History

Source: 02_nav_history.csv

| Column    | Data Type | Description     |
| --------- | --------- | --------------- |
| amfi_code | Integer   | Fund identifier |
| date      | Date      | NAV date        |
| nav       | Float     | Net Asset Value |

---

## Dataset 03 - AUM By Fund House

Source: 03_aum_by_fund_house.csv

Contains Assets Under Management data for each AMC.

---

## Dataset 04 - Monthly SIP Inflows

Contains monthly SIP inflow statistics.

---

## Dataset 05 - Category Inflows

Contains category-wise fund inflows.

---

## Dataset 06 - Industry Folio Count

Contains industry folio count statistics.

---

## Dataset 07 - Scheme Performance

Contains return, risk and performance metrics.

---

## Dataset 08 - Investor Transactions

Contains investor transaction records.

---

## Dataset 09 - Portfolio Holdings

Contains scheme portfolio composition.

---

## Dataset 10 - Benchmark Indices

Contains benchmark performance history.
