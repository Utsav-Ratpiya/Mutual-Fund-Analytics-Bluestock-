-- Query 1
-- Top 5 Fund Houses by AUM

SELECT
fund_house,
SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;


-- Query 2
-- Average NAV Per Month

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- Query 3
-- SIP Year-over-Year Growth

SELECT
strftime('%Y', transaction_date) AS year,
SUM(amount_inr) AS sip_amount
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY year;


-- Query 4
-- Transactions By State

SELECT
state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- Query 5
-- Funds With Expense Ratio Below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;


-- Query 6
-- Top 10 Funds By 5-Year Return

SELECT
amfi_code,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- Query 7
-- Average Expense Ratio By Category

SELECT
category,
AVG(expense_ratio_pct)
FROM dim_fund
GROUP BY category;


-- Query 8
-- Transaction Volume By Type

SELECT
transaction_type,
SUM(amount_inr)
FROM fact_transactions
GROUP BY transaction_type;


-- Query 9
-- Risk Category Distribution

SELECT
risk_grade,
COUNT(*)
FROM fact_performance
GROUP BY risk_grade;


-- Query 10
-- Payment Mode Analysis

SELECT
payment_mode,
COUNT(*)
FROM fact_transactions
GROUP BY payment_mode;