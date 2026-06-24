import sqlite3
import pandas as pd

conn = sqlite3.connect("../bluestock_mf.db")

query = """
SELECT
fund_house,
SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;
"""

result = pd.read_sql(query, conn)

print(result)

conn.close()