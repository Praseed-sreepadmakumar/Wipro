import pandas as pd

df = pd.read_excel("sales_data.xlsx", sheet_name="2025")

df["Total"] = df["Quantity"] * df["Price"]

df.to_excel("sales_summary.xlsx", index=False)

print("sales_summary.xlsx file created successfully!")
