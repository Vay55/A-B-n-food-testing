# Fast Food Marketing Promotion A/B/n Testing Analysis

## Project Overview

This project analyzes the effectiveness of three different promotional marketing strategies used by a fast-food company to promote a newly introduced menu item.

The objective of the experiment was to determine:
- which promotion generated the strongest sales performance
- whether the observed differences were statistically significant
- whether market conditions influenced promotional effectiveness

This project follows a complete A/B/n testing workflow involving:
- data validation
- SQL analysis
- exploratory data analysis
- statistical testing
- segmentation analysis
- business interpretation

The experiment compares:
- Promotion 1
- Promotion 2
- Promotion 3

using weekly sales data collected across multiple store locations and market sizes.

Raw data was taken from a Kaggle dataset.

---

# Business Problem

A fast-food company introduced a new menu item and tested three separate promotional campaigns across different store locations.

The company wanted to determine:
- which promotion strategy generated the highest sales
- whether sales differences were statistically significant
- whether market conditions influenced promotion performance
- which strategy would be most suitable for large-scale deployment

---

# Experiment Design

This project represents a multi-variant A/B test (A/B/n test), where multiple treatment groups are compared simultaneously.

## Independent Variable
Promotion strategy:
- Promotion 1
- Promotion 2
- Promotion 3

## Dependent Variable
`SalesInThousands`

This variable measures the weekly sales performance of the promoted item.

---

# Dataset Information

## Dataset Columns

| Column | Description |
|---|---|
| MarketID | Unique market identifier |
| MarketSize | Size of market area |
| LocationID | Unique store location |
| AgeOfStore | Store age in years |
| Promotion | Promotion strategy used |
| week | Week of experiment |
| SalesInThousands | Weekly sales amount |

## Dataset Size

- 548 rows
- 7 columns

---

# Technologies Used

- Python
- SQLite
- pandas
- SciPy
- statsmodels
- Matplotlib
- Tableau

---

# Workflow

## 1. Data Loading and Validation

The dataset was imported into SQLite and validated using SQL queries.

### Validation Checks
- missing values
- duplicate records
- promotion group distribution
- dataset integrity

### Validation Results

#### Dataset Shape

| Metric | Value |
|---|---|
| Rows | 548 |
| Columns | 7 |

#### Missing Values Check
No missing values were detected in the dataset.

#### Duplicate Check
No duplicate experiment records were detected.

#### Promotion Group Distribution

| Promotion | Total Records |
|---|---|
| 1 | 172 |
| 2 | 188 |
| 3 | 188 |

The experiment groups were relatively balanced, allowing for more reliable statistical analysis.

---

# 2. Exploratory Data Analysis

Initial analysis focused on:
- average sales by promotion
- sales variability
- distribution analysis
- weekly trends
- market segmentation

---

# Average Sales by Promotion

| Promotion | Average Sales |
|---|---|
| 1 | 58.10 |
| 2 | 47.33 |
| 3 | 55.36 |

## Initial Observations

- Promotion 1 achieved the highest average sales
- Promotion 2 consistently underperformed
- Promotion 3 performed similarly to Promotion 1

---

# Standard Deviation Analysis

| Promotion | Standard Deviation |
|---|---|
| 1 | 16.55 |
| 2 | 15.11 |
| 3 | 16.77 |

## Observations

- Promotion 3 showed the highest variability
- Promotion 2 produced the most stable but weakest performance
- Promotion 1 demonstrated strong and relatively stable performance

---

# Boxplot Analysis

Boxplots were used to visualize:
- sales distributions
- spread
- outliers
- overlap between promotions

<img width="638" height="475" alt="Screenshot 2026-05-23 at 15 32 04" src="https://github.com/user-attachments/assets/ae2841e0-fabc-4654-bde3-ef551cade250" />

## Key Insights

- Promotions 1 and 3 showed significant overlap
- Promotion 2 consistently exhibited lower performance
- Promotion 3 displayed larger variability across locations

---

# Statistical Testing

## ANOVA Test

ANOVA was performed to determine whether the differences between promotion groups were statistically significant.

### ANOVA Results

| Metric | Value |
|---|---|
| F-statistic | 21.95 |
| p-value | 6.77 × 10^-10 |

### Conclusion

Since:

```math
p < 0.05
```

the null hypothesis was rejected.

This indicates that at least one promotion strategy produced significantly different sales results.

---

# Tukey HSD Post-Hoc Testing

Pairwise comparisons were conducted to determine which promotions differed significantly.

| Comparison | Mean Difference | p-adjusted | Significant Difference |
|---|---|---|---|
| Promotion 1 vs 2 | -10.77 | 0.0 | Yes |
| Promotion 1 vs 3 | -2.73 | 0.2444 | No |
| Promotion 2 vs 3 | 8.04 | 0.0 | Yes |

## Interpretation

- Promotion 2 significantly underperformed against both Promotions 1 and 3
- Promotions 1 and 3 were not statistically different
- Promotion 1 maintained slightly stronger numerical performance overall

---

# Market Size Segmentation Analysis

Average sales were analyzed across:
- Large markets
- Medium markets
- Small markets

## Market Size Results

| Promotion | Market Size | Average Sales |
|---|---|---|
| 3 | Large | 77.20 |
| 1 | Large | 75.24 |
| 2 | Large | 60.32 |
| 1 | Medium | 47.67 |
| 3 | Medium | 45.47 |
| 2 | Medium | 39.11 |
| 1 | Small | 60.16 |
| 3 | Small | 59.51 |
| 2 | Small | 50.81 |

## Key Findings

- Promotion 2 consistently underperformed across all market sizes
- Promotions 1 and 3 remained closely competitive
- Large markets generated substantially higher sales overall

This suggests:
- market size strongly influences sales performance
- Promotion 1 demonstrated stronger overall scalability

---

# Weekly Trend Analysis

Weekly average sales were analyzed across the four-week experiment period.

## Weekly Results

| Week | Promotion | Average Sales |
|---|---|---|
| 1 | 1 | 58.24 |
| 1 | 2 | 47.73 |
| 1 | 3 | 55.78 |
| 2 | 1 | 56.93 |
| 2 | 2 | 47.58 |
| 2 | 3 | 55.95 |
| 3 | 1 | 58.77 |
| 3 | 2 | 47.72 |
| 3 | 3 | 54.38 |
| 4 | 1 | 58.45 |
| 4 | 2 | 46.28 |
| 4 | 3 | 55.35 |

## Weekly Trend Insights

- Promotion 1 consistently maintained the highest weekly sales
- Promotion 3 remained close behind throughout all weeks
- Promotion 2 consistently performed worst

This reinforced the reliability of Promotion 1’s performance.

---

# Dashboard 

This dashboard was developed in Google Looker studio to visualize the results of the A/B/n testing analysis conducted on three fast-food promotional strategies.

<img width="882" height="626" alt="Screenshot 2026-05-23 at 23 44 52" src="https://github.com/user-attachments/assets/b5e998ec-cf11-4488-a5bf-77da9cf05e57" />

---

# Business Interpretation

## Promotion 1

### Strengths
- highest overall sales
- stable weekly performance
- strong consistency across markets

### Potential Risks
- not statistically superior to Promotion 3
- moderate variability still exists
- long-term effectiveness remains uncertain

---

## Promotion 3

### Strengths
- competitive sales performance
- strong upside potential in some markets

### Potential Risks
- highest variability
- less predictable performance
- may depend more heavily on market conditions

---

## Promotion 2

### Strengths
- relatively stable performance

### Weaknesses
- consistently weakest sales results
- significantly underperformed against both alternatives

---

# Experiment Limitations

Several limitations may affect the generalizability of the findings.

## Short Experiment Duration

The experiment only covered four weeks.

This may not fully capture:
- long-term customer behavior
- sustained engagement
- long-term ROI
- customer retention

There is also a possibility that:
- Promotion 3 may perform better over a longer testing period
- Promotion 2 may perform more effectively during seasonal or event-specific conditions

---

## Seasonal and Environmental Factors

External conditions may have influenced results, including:
- seasonal variability
- weather conditions
- local economic conditions
- consumer behavior trends

---

## Missing Variables

The dataset did not include:
- campaign costs
- customer demographics
- customer retention
- repeat purchases
- profitability metrics

Therefore, sales alone may not fully represent overall marketing effectiveness.

---

# Final Recommendation

Based on the experimental analysis:

- Promotion 2 should likely not be selected for broad deployment due to consistently weaker performance.
- Promotions 1 and 3 both demonstrated strong results.
- Promotion 1 appears to be the safest and most reliable option for large-scale deployment due to:
  - highest average sales
  - stable weekly performance
  - stronger consistency across market sizes

However:
- Promotion 3 may warrant additional long-term testing due to its competitive performance and potential growth under different market conditions.

---

# Future Improvements

Potential future analysis could include:
- longer-duration experiments
- seasonal testing
- customer demographic segmentation
- ROI/profitability analysis
- customer retention analysis
- regional behavior analysis

---

# Project Skills Demonstrated

This project demonstrates:
- SQL querying
- data validation
- exploratory data analysis
- A/B/n testing methodology
- statistical hypothesis testing
- ANOVA analysis
- post-hoc testing
- data visualization
- business interpretation
- experimental limitation analysis
- dashboard preparation using Google looker studio

---
Data from https://www.kaggle.com/datasets/chebotinaa/fast-food-marketing-campaign-ab-test
