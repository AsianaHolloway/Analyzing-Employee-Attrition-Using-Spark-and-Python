"""
Employee_Attrition_Analysis.py

This script performs end-to-end preprocessing and analysis of the IBM HR Analytics Employee Attrition dataset using Apache Spark.
It includes steps for data cleaning, feature selection, and insights into employee turnover trends. 
The goal is to explore factors contributing to attrition to support strategic HR decisions.
"""

Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> !unzip /home/sat3812/Downloads/archive.zip -d /home/sat3812/Downloads/
... 
... from pyspark.sql import SparkSession
... spark = SparkSession.builder.appName("Employee Attrition Analysis").getOrCreate()
... 
... df = spark.read.csv("/home/sat3812/employee_attrition/WA_Fn-UseC_-HR-Employee-Attrition.csv", header=True, inferSchema=True)
... 
... df.printSchema()
... df = df.dropna()
... 
... df.describe().show()
... 
... df_pandas = df.select("Attrition").toPandas()
... 
... import matplotlib.pyplot as plt
... 
... attrition_counts = df_pandas["Attrition"].value_counts()
... attrition_counts.plot(kind='bar')
... plt.xlabel('Attrition')
... plt.ylabel('Number of Employees')
... plt.title('Employee Attrition Count')
... plt.show()
