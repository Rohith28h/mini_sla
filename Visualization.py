# Product Sales Comparison (Bar Chart)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv('minmini.csv')
# Product-wise sales
product_sales = df.groupby("Product")["Sales"].sum()
plt.figure(figsize=(8,5))
# Create bar chart
plt.bar(product_sales.index, product_sales.values)

plt.title("Product Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Total Sales")

# Show graph
plt.show()

# Product-wise profit
product_profit = df.groupby("Product")["Profit"].sum()

# Figure size
plt.figure(figsize=(8,5))

# Bar chart
plt.bar(product_profit.index, product_profit.values)

# Title and labels
plt.title("Product Profit Comparison")
plt.xlabel("Products")
plt.ylabel("Total Profit")

# Show graph
plt.show()

# Figure size
plt.figure(figsize=(10,5))

# Line chart
plt.plot(df["Order_ID"], df["Sales"])

# Title and labels
plt.title("Sales Trend Analysis")
plt.xlabel("Order ID")
plt.ylabel("Sales")

# Show graph
plt.show()

# Product-wise profit
product_profit = df.groupby("Product")["Profit"].sum()

# Figure size
plt.figure(figsize=(7,7))

# Pie chart
plt.pie(product_profit.values,
        labels=product_profit.index,
        autopct="%1.1f%%")

# Title
plt.title("Profit Distribution by Product")

# Show graph
plt.show()

# Figure size
plt.figure(figsize=(8,5))

# Histogram
plt.hist(df["Sales"], bins=5)
# Title and labels
plt.title("Sales Distribution")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")

# Show graph
plt.show()