# 📊 Analyzing Employee Attrition Using Spark and Python

## Project Overview

Employee attrition can reveal hidden issues in a workplace from poor job satisfaction to work-life balance challenges. This project aims to uncover key factors that influence employee turnover using **PySpark** and a **linear regression model**. Built as part of my graduate coursework in **Big Data Analytics**, it demonstrates my ability to set up a dual-node Spark environment, perform data preprocessing, and extract meaningful insights from large datasets.

---

## 👨‍💻 Tools & Technologies

- **Apache Spark** (with dual-VM cluster: Hadoop1 as NameNode, Hadoop2 as DataNode)
- **PySpark** for distributed data processing
- **Pandas** & **Matplotlib** for visualization
- **Scikit-learn** for regression modeling

---

## 🗂 Dataset

- **IBM HR Analytics Employee Attrition Dataset**  
  📥 [View Dataset on Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)  
  Records: 1,470+ employee profiles including fields like:
  - Age
  - Job Role
  - Monthly Income
  - Work-Life Balance
  - Job Satisfaction
  - Attrition Status

---


## 🔍 Objectives

- ✅ Preprocess and clean data (remove missing values, label encode categories)
- ✅ Load dataset into Spark DataFrames using PySpark
- ✅ Analyze key variables using linear regression
- ✅ Visualize attrition counts using Pandas & Matplotlib
- ✅ Compare single-VM vs. dual-VM Spark performance

---

## 📈 Key Insights

- Identified correlations between **Monthly Income**, **Job Satisfaction**, and **Attrition**
- Regression modeling revealed key predictive features of employee turnover
- Data visualization clearly illustrated attrition patterns
- Running Spark in a dual-VM setup improved processing efficiency and memory usage

---

## 📷 Screenshots

- 💻 Dual-node Spark Setup
- 📊 Employee Attrition Bar Chart
- 🧹 Data Cleaning in PySpark

---

## 🧠 What I Learned

This project helped me:
- Set up and configure Spark in a virtual cluster
- Apply machine learning techniques to real-world HR data
- Use PySpark to process and analyze large datasets
- Translate insights into meaningful business recommendations

---

## 📂 Files Included

- `project_proposal.docx`: Initial planning and project scope
- `employee_analysis_report.docx`: Final analysis write-up
- `code/`: Spark and Python scripts
- `visuals/`: Screenshot folder (Spark setup, bar chart)
- `README.md`: Project summary and references

---

## 📂 Code Overview

### `Single_VM_Test.py`
Runs the machine learning pipeline on a single virtual machine using Apache Spark. It performs data preprocessing, model training, and evaluation on a standalone node to establish a performance baseline.

### `Dual_VM_Test.py`
Runs the same ML pipeline on a dual-VM Spark cluster. It distributes computation to evaluate performance scalability and speed improvements compared to the single-node setup.

---

## 📊 Result Screenshots

Screenshots in the visual file highlight runtime performance metrics captured while executing Spark jobs on single and dual VM configurations.

1. **Start:End Time Data Loading**  
   *Displays the Python terminal session showing the time measurement for data loading from CSV into Spark DataFrame using PySpark.*

2. **Data Loading Time (Single VM)**  
   *Shows the output of the time taken to load the dataset into Spark on a single VM node—used to benchmark loading performance.*

3. **Data Cleaning Time (Single VM)**  
   *Illustrates the duration required to clean the data (dropping nulls) on a single VM environment.*

4. **Data Analysis Time (Single VM)**  
   *Displays the execution time for analyzing employee attrition counts on a single VM using Spark.*

5. **Data Loading Time (Dual VM)**  
   *Shows the output of loading the dataset on a dual-VM Spark environment to compare against single VM performance.*

6. **Data Cleaning Time (Dual VM)**  
   *Displays the duration of the data cleaning operation across a dual-VM cluster.*

7. **Data Analysis Time (Dual VM)**  
   *Shows time required to perform employee attrition group analysis on a dual-VM Spark setup.*
---

## 🔗 Additional Resources

- 🗃️ [Kaggle Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)  
- 📄 [Final Project Report (Google Drive)](https://drive.google.com/file/d/1IVZsBk37MifbOHTgSiFh0dqButzFqaV9/view?usp=drive_link)

---

Author
Asiana Holloway 
Graduate Student – Big Data Analytics
GitHub: [AsianaHolloway](https://github.com/AsianaHolloway)

