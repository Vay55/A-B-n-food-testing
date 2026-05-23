import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import f_oneway
import pandas as pd
import sqlite3

df = pd.read_csv("raw_data/WA_Marketing-Campaign.csv")

#Checks
print(df.head())
print(df.shape)
print(df.info())

#Database connection
conn = sqlite3.connect("ab_testing.db")

df.to_sql(
    "marketing_campaign",
    conn,
    if_exists="replace",
    index=False
)

#SQL QUERIES

    ##total rows
query = """
SELECT COUNT(*) AS total_rows
FROM marketing_campaign
"""

result = pd.read_sql(query, conn)
print(result)

    ##preview table
query = """
SELECT *
FROM marketing_campaign
LIMIT 10
"""

result = pd.read_sql(query, conn)
print(result)


    ##check missing values
query = """
SELECT *
FROM marketing_campaign
WHERE
    MarketID IS NULL
    OR MarketSize IS NULL
    OR LocationID IS NULL
    OR AgeOfStore IS NULL
    OR Promotion IS NULL
    OR week IS NULL
    OR SalesInThousands IS NULL
"""

result = pd.read_sql(query, conn)
print(result)

    ##duplicate records
query = """
SELECT
    MarketID,
    LocationID,
    Promotion,
    week,
    COUNT(*) AS duplicate_count
FROM marketing_campaign
GROUP BY
    MarketID,
    LocationID,
    Promotion,
    week
HAVING COUNT(*) > 1
"""

result = pd.read_sql(query, conn)
print(result)

    ##promotion distribution
query = """
SELECT
    Promotion,
    COUNT(*) AS total_records
FROM marketing_campaign
GROUP BY Promotion
"""

result = pd.read_sql(query, conn)
print(result)

    ##initial avg sales comparision
query = """
SELECT
    Promotion,
    ROUND(AVG(SalesInThousands), 2) AS avg_sales
FROM marketing_campaign
GROUP BY Promotion
ORDER BY avg_sales DESC
"""

result = pd.read_sql(query, conn)
print(result)

#variability
std_analysis = df.groupby("Promotion")["SalesInThousands"].agg(
    avg_sales="mean",
    sales_stddev="std"
).round(2)

print(std_analysis)


#Graph
"""
df.boxplot(
    column="SalesInThousands",
    by="Promotion",
    grid=False
)

plt.title("Sales Distribution by Promotion")
plt.suptitle("")
plt.xlabel("Promotion")
plt.ylabel("Sales In Thousands")

plt.show()
"""

#anova
promotion_1 = df[df["Promotion"] == 1]["SalesInThousands"]
promotion_2 = df[df["Promotion"] == 2]["SalesInThousands"]
promotion_3 = df[df["Promotion"] == 3]["SalesInThousands"]

anova_result = f_oneway(
    promotion_1,
    promotion_2,
    promotion_3
)

print(anova_result)


#pairwise testing
tukey = pairwise_tukeyhsd(
    endog=df["SalesInThousands"],
    groups=df["Promotion"],
    alpha=0.05
)

print(tukey)


#avg sales with market size and promotion
query = """
SELECT
    Promotion,
    MarketSize,
    ROUND(AVG(SalesInThousands), 2) AS avg_sales
FROM marketing_campaign
GROUP BY Promotion, MarketSize
ORDER BY MarketSize, avg_sales DESC
"""

market_analysis = pd.read_sql(query, conn)

print(market_analysis)

#weekly trends
query = """
SELECT
    week,
    Promotion,
    ROUND(AVG(SalesInThousands), 2) AS avg_sales
FROM marketing_campaign
GROUP BY week, Promotion
ORDER BY week, Promotion
"""

weekly_analysis = pd.read_sql(query, conn)

print(weekly_analysis)


#aggregate into 3 files
market_analysis.to_csv(
    "market_analysis.csv",
    index=False
)

weekly_analysis.to_csv(
    "weekly_analysis.csv",
    index=False
)

std_analysis.reset_index().to_csv(
    "std_analysis.csv",
    index=False
)

print("CSV export completed.")