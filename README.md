 # Project 2 - Exploratory Data Analysis

## Project Overview

This project performs Exploratory Data Analysis (EDA) on an online shopping dataset.

## Dataset

- Total Orders: 1200
- Number of Columns: 14
- Main numerical variables:
  - Quantity
  - UnitPrice
  - ItemsInCart
  - TotalPrice

## Analysis Performed

1. Data cleaning
2. Basic statistics
3. Total sales by product
4. Total sales by order status
5. Total sales by payment method
6. Outlier analysis using IQR
7. Boxplot of TotalPrice
8. Distribution of TotalPrice
9. Correlation analysis
10. Scatter plots
11. Pairplot
12. EDA summary and key observations

## Key Findings

- The dataset contains 1200 orders and 14 columns.
- The average TotalPrice is approximately 1053.97.
- The median TotalPrice is approximately 823.62.
- UnitPrice and TotalPrice have a strong positive correlation.
- Quantity and TotalPrice have a positive correlation.
- ItemsInCart and TotalPrice have a moderate positive correlation.
- There are 8 outliers in TotalPrice based on the IQR method.
- TotalPrice distribution is right-skewed.
- Chair generated the highest total sales,followed closely by printer and laptop.
- Credit Card has the highest total sales among the payment methods.
## Recommendations

- Focus on high-performing products such as Chair and Printer to improve sales.
- Monitor cancelled orders to understand the reasons for lost sales.
- Credit Card is the leading payment method, so it should be maintained and optimized.
- Investigate the identified TotalPrice outliers to determine whether they represent genuine high-value orders or unusual transactions.
- Use the relationship between UnitPrice, Quantity and TotalPrice to support better sales analysis and decision-making.

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Visual Studio Code

## Project Files

- Project_2_EDA.ipynb - EDA notebook
- eda_analysis.py - Python source code
- data/ - Dataset files
- charts/ - Generated charts
- README.md - Project documentation 