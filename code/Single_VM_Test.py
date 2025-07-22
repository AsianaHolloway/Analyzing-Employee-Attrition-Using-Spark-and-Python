"""
Single_VM_Test.py

Runs a Spark-based ML pipeline on a single VM.
Performs preprocessing, model training, and evaluation on employee attrition data.
Used to establish baseline performance before distributed testing.
"""

Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... from pyspark.sql import SparkSession
... import time
... 
... spark = SparkSession.builder.appName("Employee Attrition Analysis - Single VM").getOrCreate()
... 
... start_load_time = time.time()
... df = spark.read.csv("/home/sat3812/employee_attrition/WA_Fn-UseC_-HR-Employee-Attrition.csv", header=True, inferSchema=True)
... load_time = time.time() - start_load_time
... print(f"Data Loading Time (Single VM): {load_time:.2f} seconds")
... 
... start_clean_time = time.time()
... df_cleaned = df.dropna()
... clean_time = time.time() - start_clean_time
... print(f"Data Cleaning Time (Single VM): {clean_time:.2f} seconds")
... 
... start_analysis_time = time.time()
... attrition_counts = df_cleaned.groupBy("Attrition").count()
... attrition_counts.show()
... analysis_time = time.time() - start_analysis_time
... print(f"Data Analysis Time (Single VM): {analysis_time:.2f} seconds")
