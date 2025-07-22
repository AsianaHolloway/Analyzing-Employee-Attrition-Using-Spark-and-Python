"""
Descriptive_Analysis.py

This script generates descriptive statistics and visual summaries for the IBM HR Analytics Employee Attrition dataset.
It uses PySpark to calculate distributions, correlations, and key HR metrics to understand workforce composition and attrition patterns.
"""

Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> df.show(5)
... 
... df.agg({"MonthlyIncome": "avg"}).show()
... 
... df.agg({"YearsAtCompany": "max"}).show()
... 
... df.agg({"YearsAtCompany": "min"}).show()
