📊 Analyzing Employee Attrition Using Spark and Python
Project Overview
Employee attrition can reveal hidden issues in a workplace—from poor job satisfaction to work-life balance challenges. This project aims to uncover key factors that influence employee turnover using PySpark and a linear regression model. Built as part of my graduate coursework in Big Data Analytics, it demonstrates my ability to set up a dual-node Spark environment, perform data preprocessing, and extract meaningful insights from large datasets.

👨‍💻 Tools & Technologies
Apache Spark (with dual-VM cluster: Hadoop1 as NameNode, Hadoop2 as DataNode)

PySpark for distributed data processing

Pandas & Matplotlib for visualization

Scikit-learn for regression modeling

🗂 Dataset
IBM HR Analytics Employee Attrition Dataset
Source: Kaggle
Records: 1,470+ employee profiles including fields like:

Age

Job Role

Monthly Income

Work-Life Balance

Job Satisfaction

Attrition Status

🔍 Objectives

✅ Preprocess and clean data (remove missing values, label encode categories)

✅ Load dataset into Spark DataFrames using PySpark

✅ Analyze key variables using linear regression

✅ Visualize attrition counts using Pandas & Matplotlib

✅ Compare single-VM vs. dual-VM Spark performance

📈 Key Insights
Successfully identified correlations between Monthly Income, Job Satisfaction, and Attrition

Linear regression revealed which factors most significantly impact employee turnover

Visualization (bar chart) showed a clear split between employees who stayed and those who left

Distributed Spark setup reduced processing time and improved memory handling

📷 Screenshots
💻 Distributed Spark Setup

📊 Attrition Visualization

⚙️ Data Preprocessing in Spark

🧠 What I Learned
This project deepened my understanding of:

Setting up and managing Spark clusters

Real-world data preprocessing challenges

Combining distributed and local data tools effectively

Presenting technical insights in a clear and professional way

📂 Files Included
project_proposal.docx: Initial planning and project structure

employee_analysis_report.docx: Final project write-up

code/: Spark scripts and preprocessing code

visuals/: Bar chart and system screenshots

🔗 Related Links
📁 Dataset on Kaggle

📚 Final Report (PDF)

📬 GitHub Repo


