import pandas as pd

df = pd.read_excel("sales_data.xlsx")

df["Total"] = df["Quantity"] * df ["Unit Price"]

summary = df.groupby("Region")["Total"].sum().reset_index()

summary.to_excel("regional_sales_summary.xlsx", index=False)

print("Summary saved to 'regional_sales_summary.xlsx'")