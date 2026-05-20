import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('minmini.csv')

# Create dashboard size
plt.figure(figsize=(15,10))

# --------------------------
# 1. Product Sales Chart
# --------------------------
plt.subplot(2,2,1)

product_sales = df.groupby("Product")["Sales"].sum()

plt.bar(product_sales.index,
        product_sales.values)

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

# --------------------------
# 2. Product Profit Chart
# --------------------------
plt.subplot(2,2,2)

product_profit = df.groupby("Product")["Profit"].sum()

plt.bar(product_profit.index,
        product_profit.values)

plt.title("Product Profit")
plt.xlabel("Products")
plt.ylabel("Profit")

# --------------------------
# 3. Sales Trend
# --------------------------
plt.subplot(2,2,3)

plt.plot(df["Order_ID"],
         df["Sales"])

plt.title("Sales Trend")
plt.xlabel("Order ID")
plt.ylabel("Sales")

# --------------------------
# 4. Profit Distribution
# --------------------------
plt.subplot(2,2,4)

plt.pie(product_profit.values,
        labels=product_profit.index,
        autopct="%1.1f%%")

plt.title("Profit Distribution")

# Adjust spacing
plt.tight_layout()

# Show dashboard
plt.show()