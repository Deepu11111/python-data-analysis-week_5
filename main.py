import pandas as pd

# 1. Load Data
sales = pd.read_csv("sales.csv")
customers = pd.read_csv("customers.csv")

#sales.columns = sales.columns.str.strip()
#customers.columns = customers.columns.str.strip()

print("\nOriginal Data\n",sales)

# 2. Convert Date to datetime

sales["Date"] = pd.to_datetime(sales["Date"])

# 3.Extract year , month , day

sales["Year"] = sales["Date"].dt.year
sales["Month"] = sales["Date"].dt.month
sales["Day"] = sales["Date"].dt.day

print("\nDate Part added\n",sales)

# 4. Group by month - monthly totals
monthly_sales = sales.groupby("Month")["Total_Sales"].sum()
print("\nMonthly Sales Totals\n",monthly_sales)

# 5.Multiple condition filtering
# Example : North region AND Sales > 20000

filtered = sales[(sales["Region"]== "North") & (sales["Total_Sales"] > 20000)]
print("\nFiltered Data\n",filtered)

# 6. String cleaning
sales["Product"] = sales["Product"].str.upper()
print("\nProduct names upper case\n",sales["Product"])

# 7. Merge Customers with sales

sales["Customer_ID"] = sales["Customer_ID"].str.strip()
merged = pd.merge(sales, customers, left_on="Customer_ID", right_on="CustomerID", how="inner")


print("\nMerged Data\n",merged)

# 8. Pivot table
pivot = pd.pivot_table(
    merged,
    values="Total_Sales",
    index="Product",
    columns="Region",
    aggfunc="sum"
)

print("\nPivot Table\n",pivot)