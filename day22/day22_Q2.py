import pandas as pd
import numpy as np


df = pd.read_csv("sales.csv")


df["Date"] = pd.to_datetime(df["Date"])


df["Total"] = df["Quantity"] * df["Price"]

print("Updated DataFrame:")
print(df)


# Total sales
total_sales = np.sum(df["Total"].values)

# Average daily sales
average_daily_sales = np.mean(df["Total"].values)

# Standard deviation of daily sales
std_daily_sales = np.std(df["Total"].values)

print("\nSales Statistics:")
print("Total Sales:", total_sales)
print("Average Daily Sales:", average_daily_sales)
print("Standard Deviation of Daily Sales:", std_daily_sales)


product_sales = df.groupby("Product")["Quantity"].sum()
best_selling_product = product_sales.idxmax()

print("\nBest Selling Product:", best_selling_product)
print("Total Quantity Sold:", product_sales[best_selling_product])
