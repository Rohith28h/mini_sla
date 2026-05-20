import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('minmini.csv')

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

avg_sales = df["Sales"].mean()
avg_profit = df["Profit"].mean()

best_product = df.groupby("Product")["Sales"].sum().idxmax()
highest_profit_product = df.groupby("Product")["Profit"].sum().idxmax()

product_sales = df.groupby("Product")["Sales"].sum()
product_profit = df.groupby("Product")["Profit"].sum()

region_sales = df.groupby("Region")["Sales"].sum()

best_region = region_sales.idxmax()

while True:

    print("\n===== RETAIL SALES ANALYTICS DASHBOARD =====")

    print("1. View Total Sales & Profit")
    print("2. Product Analysis")
    print("3. Region Analysis")
    print("4. Show Dashboard")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # ----------------------------------
    # Option 1
    # ----------------------------------
    if choice == 1:

        print("\n----- SALES REPORT -----")

        print("Total Sales :", total_sales)
        print("Total Profit :", total_profit)

        print("Average Sales :",
              round(avg_sales, 2))

        print("Average Profit :",
              round(avg_profit, 2))

    # ----------------------------------
    # Option 2
    # ----------------------------------
    elif choice == 2:

        print("\n----- PRODUCT ANALYSIS -----")

        print("Best Selling Product :",
              best_product)

        print("Highest Profit Product :",
              highest_profit_product)

        print("\nProduct Sales")

        print(product_sales)

    # ----------------------------------
    # Option 3
    # ----------------------------------
    elif choice == 3:

        print("\n----- REGION ANALYSIS -----")

        print(region_sales)

        print("\nMost Profitable Region :",
              best_region)

        # ----------------------------------
    # Option 4
    # ----------------------------------
    elif choice == 4:

        print("\nOpening Dashboard...")

        # Create dashboard size
        plt.figure(figsize=(16, 10))

        # ==========================
        # 1. Product Sales Chart
        # ==========================
        plt.subplot(2, 2, 1)

        top_product = product_sales.idxmax()

        colors = ['skyblue' if product != top_product
                  else 'orange'
                  for product in product_sales.index]

        bars = plt.bar(product_sales.index,
                       product_sales.values,
                       color=colors)

        plt.title("Product Sales Comparison",
                  fontsize=12)

        plt.xlabel("Products")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=20)

        # Value labels
        for bar in bars:
            plt.text(bar.get_x() + bar.get_width()/2,
                     bar.get_height(),
                     f'{bar.get_height():.0f}',
                     ha='center',
                     fontsize=8)

        # ==========================
        # 2. Product Profit Chart
        # ==========================
        plt.subplot(2, 2, 2)

        top_product = product_profit.idxmax()

        colors = ['lightblue' if product != top_product
                  else 'green'
                  for product in product_profit.index]

        bars = plt.bar(product_profit.index,
                       product_profit.values,
                       color=colors)

        plt.title("Product Profit Comparison",
                  fontsize=12)

        plt.xlabel("Products")
        plt.ylabel("Total Profit")
        plt.xticks(rotation=20)

        # Value labels
        for bar in bars:
            plt.text(bar.get_x() + bar.get_width()/2,
                     bar.get_height(),
                     f'{bar.get_height():.0f}',
                     ha='center',
                     fontsize=8)

        # ==========================
        # 3. Sales Trend
        # ==========================
        plt.subplot(2, 2, 3)

        plt.plot(df["Order_ID"],
                 df["Sales"],
                 marker='o',
                 linewidth=1)

        plt.title("Sales Trend",
                  fontsize=12)

        plt.xlabel("Order ID")
        plt.ylabel("Sales")

        plt.grid(True,
                 linestyle="--",
                 alpha=0.7)

        # ==========================
        # 4. Profit Distribution
        # ==========================
        plt.subplot(2, 2, 4)

        profit_distribution = df.groupby("Product")["Profit"].sum()

        explode = [0.1 if value == profit_distribution.max()
                   else 0
                   for value in profit_distribution.values]

        plt.pie(profit_distribution.values,
                labels=profit_distribution.index,
                autopct='%1.1f%%',
                explode=explode)

        

        plt.title("Profit Distribution",
                  fontsize=12)

        # Adjust spacing
        plt.tight_layout()

        # Show dashboard
        plt.show()
    

    # ----------------------------------
    # Option 5
    # ----------------------------------
    elif choice == 5:

        print("\nThank You!")
        print("Exiting Dashboard...")

        break

    else:

        print("\nInvalid Choice!")
        print("Please enter 1 to 5.")