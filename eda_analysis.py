# %%
#%pip install pandas numpy matplotlib seaborn openpyxl

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
print("Hello")

# %%
# Load the dataset
df = pd.read_excel("data/Dataset for Data Analytics.xlsx")

# Display the first 5 rows
df.head()

# %%
# Check dataset information
df.info()

# %%
# Check for missing values
df.isnull().sum()

# %%
# Check for duplicate rows
df.duplicated().sum()

# %%
# Fill missing coupon codes
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')

# Check missing values again
df.isnull().sum()

# %%
# Check statistical summary
df.describe()

# %%
# Check unique values in categorical columns

print("Products:")
print(df['Product'].unique())

print("\nPayment Methods:")
print(df['PaymentMethod'].unique())

print("\nOrder Status:")
print(df['OrderStatus'].unique())

# %%
# Count orders by product
product_counts = df['Product'].value_counts()

print(product_counts)

# %%
# Bar chart - Orders by Product

import matplotlib.pyplot as plt

product_counts = df['Product'].value_counts()

plt.figure(figsize=(8,5))
product_counts.plot(kind='bar')
plt.title('Number of Orders by Product')
plt.xlabel('Product')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('Charts/orders_by_product.png')
plt.show()

# %%
# Count orders by payment method

payment_counts = df['PaymentMethod'].value_counts()

print(payment_counts)

# %%
# Bar chart - Orders by Payment Method

plt.figure(figsize=(8, 5))

payment_counts.plot(kind='bar')

plt.title('Number of Orders by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig('Charts/orders_by_payment_method.png')
plt.show()

# %%
# Count orders by order status
status_counts = df['OrderStatus'].value_counts()

print(status_counts)

# %%
# Bar chart - Orders by Order Status

status_counts.plot(kind='bar', figsize=(8,5))

plt.title('Number of Orders by Order Status')
plt.xlabel('Order Status')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig('Charts/orders_by_order_status.png')
plt.show()

# %%
# Bar chart - Orders by Payment Method

payment_counts = df['PaymentMethod'].value_counts()

plt.figure(figsize=(8,5))
payment_counts.plot(kind='bar')

plt.title('Number of Orders by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Number of Orders')
plt.xticks(rotation=0)

plt.show()

# %%
# Bar chart - Orders by Payment Method

payment_counts = df['PaymentMethod'].value_counts()

plt.figure(figsize=(8,5))
payment_counts.plot(kind='bar')

plt.title('Number of Orders by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Number of Orders')
plt.xticks(rotation=0)

plt.show()

# %%
# Bar chart - Orders by Order Status

order_status_counts = df['OrderStatus'].value_counts()

plt.figure(figsize=(8,5))
plt.bar(order_status_counts.index, order_status_counts.values)

plt.title('Number of Orders by Order Status')
plt.xlabel('Order Status')
plt.ylabel('Number of Orders')
plt.xticks(rotation=0)

plt.show()

# %%
# Bar chart - Orders by Order Status

order_status_counts = df['OrderStatus'].value_counts()

plt.figure(figsize=(8,5))
plt.bar(order_status_counts.index, order_status_counts.values)

plt.title('Number of Orders by Order Status')
plt.xlabel('Order Status')
plt.ylabel('Number of Orders')
plt.xticks(rotation=0)

plt.show()

# %%
# Bar chart - Orders by Order Status

order_status_counts = df['OrderStatus'].value_counts()

plt.figure(figsize=(8,5))
plt.bar(order_status_counts.index, order_status_counts.values)

plt.title('Number of Orders by Order Status')
plt.xlabel('Order Status')
plt.ylabel('Number of Orders')
plt.xticks(rotation=0)

plt.show()

# %%
# Total sales by product
product_sales = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False)

print(product_sales)

# %%
# Total sales by order status
status_sales = df.groupby('OrderStatus')['TotalPrice'].sum().sort_values(ascending=False)

print(status_sales)

# %%
# Total sales by payment method
payment_sales = df.groupby('PaymentMethod')['TotalPrice'].sum().sort_values(ascending=False)

print(payment_sales)

# %%
# Total sales by payment method
payment_sales = df.groupby('PaymentMethod')['TotalPrice'].sum().sort_values(ascending=False)

print(payment_sales)
# %%
# Basic statistics for TotalPrice

print("Count of TotalPrice:")
print(df['TotalPrice'].count())

print("\nMean of TotalPrice:")
print(df['TotalPrice'].mean())

print("\nMedian of TotalPrice:")
print(df['TotalPrice'].median())

print("\nMinimum TotalPrice:")
print(df['TotalPrice'].min())

print("\nMaximum TotalPrice:")
print(df['TotalPrice'].max())

print("\nStandard Deviation of TotalPrice:")
print(df['TotalPrice'].std())
# %%
# Outlier analysis using IQR

Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[(df['TotalPrice'] < lower_limit) |
              (df['TotalPrice'] > upper_limit)]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("Number of outliers:", len(outliers))
# %%
# Boxplot of TotalPrice

plt.figure(figsize=(8, 5))
sns.boxplot(x=df['TotalPrice'])
plt.title('Boxplot of TotalPrice')
plt.xlabel('Total Price')
plt.show()
# %%
# Distribution of TotalPrice

plt.figure(figsize=(8, 5))
sns.histplot(df['TotalPrice'], bins=30, kde=True)

plt.title('Distribution of TotalPrice')
plt.xlabel('Total Price')
plt.ylabel('Frequency')

plt.show()
# %%
# Correlation analysis

correlation = df[['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']].corr()

print("Correlation Matrix:")
print(correlation)

# Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')

plt.title('Correlation Matrix')
plt.show()
# %%
# Scatter plot - Quantity vs TotalPrice

plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Quantity'], y=df['TotalPrice'])

plt.title('Quantity vs TotalPrice')
plt.xlabel('Quantity')
plt.ylabel('Total Price')

plt.show()
# %%
# Scatter plot - UnitPrice vs TotalPrice

plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['UnitPrice'], y=df['TotalPrice'])

plt.title('UnitPrice vs TotalPrice')
plt.xlabel('Unit Price')
plt.ylabel('Total Price')

plt.show()
# %%
# Scatter plot - ItemsInCart vs TotalPrice

plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['ItemsInCart'], y=df['TotalPrice'])

plt.title('ItemsInCart vs TotalPrice')
plt.xlabel('Items in Cart')
plt.ylabel('Total Price')

plt.show()
# %%
# Pairplot of numerical variables

sns.pairplot(df[['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']])

plt.show()
# %%
# Save cleaned dataset

df.to_excel('data/cleaned_dataset.xlsx', index=False)

print("Cleaned dataset saved successfully.")
# %%
# EDA Summary

print("EDA SUMMARY")
print("=" * 40)

print("\n1. Dataset Shape:")
print(df.shape)

print("\n2. Total Orders:")
print(len(df))

print("\n3. Average Total Price:")
print(df['TotalPrice'].mean())

print("\n4. Highest Total Price:")
print(df['TotalPrice'].max())

print("\n5. Lowest Total Price:")
print(df['TotalPrice'].min())

print("\n6. Number of Outliers:")
print(len(outliers))
# %%
# Key Observations

print("KEY OBSERVATIONS")
print("=" * 40)

print("1. The dataset contains 1200 orders and 14 columns.")

print("2. The average TotalPrice is approximately 1053.97.")

print("3. The median TotalPrice is approximately 823.62.")

print("4. UnitPrice and TotalPrice have a strong positive correlation of about 0.72.")

print("5. Quantity and TotalPrice have a positive correlation of about 0.62.")

print("6. ItemsInCart and TotalPrice have a moderate positive correlation of about 0.39.")

print("7. There are 8 outliers in TotalPrice based on the IQR method.")

print("8. TotalPrice distribution is right-skewed, with a small number of high-value orders.")

print("9. Chair and Printer have the highest total sales among the products.")

print("10. Credit Card has the highest total sales among payment methods.")
# %%
