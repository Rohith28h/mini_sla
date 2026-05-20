import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv('minmini.csv')

# print(df.head())
# print("Shape of Dataset:", df.shape)
# print("Columns:", df.columns)
# print(df.dtypes)
# print(df.info())
# Data Quality Check
# print("null values",df.isnull().sum())
# print("Statistical Summary",df.describe())
# print("Duplicate Rows:", df.duplicated().sum())

# data to business details
tot_sales=df['Sales'].sum()
tot_profit=df['Profit'].sum()

print("Total Sales:",tot_sales)
print("Total Profit:",tot_profit)

avg_sales = df["Sales"].mean()
avg_profit = df["Profit"].mean()

print("Average Sales:", avg_sales)
print("Average Profit:", avg_profit)





# best sales
best_sales=df.groupby("Product")["Sales"].sum()
print("best product",best_sales)
#best product
best_product = best_sales.idxmax()#provides the name and the best one of the product

print("Best Selling Product:", best_product)

#pro profit
product_profit = df.groupby("Product")["Profit"].sum()

highest_profit_product = product_profit.idxmax()

print("Highest Profit Product:", highest_profit_product)

#reg sales
region_sales = df.groupby("Region")["Sales"].sum()

print(region_sales)

# Sort in descending order by profit
top_products = product_profit.sort_values(ascending=False)

print(top_products)
# by sales
top_products_sales = best_sales.sort_values(ascending=False)

print(top_products_sales)

# Region-wise Profit
region_profit = df.groupby("Region")["Profit"].sum()

print(region_profit)
best_region = region_profit.idxmax()

print("Most Profitable Region:", best_region)

# profit_percentage
profit_percentage = (tot_profit / tot_sales) * 100

print("Profit Percentage:", profit_percentage)

print("\n----- BUSINESS SUMMARY -----")

print("Total Sales:", tot_sales)
print("Total Profit:", tot_profit)
print("Best Selling Product:", best_product)
print("Highest Profit Product:", highest_profit_product)
print("Best Region:", best_region)
print("Profit Percentage:", round(profit_percentage, 2), "%")