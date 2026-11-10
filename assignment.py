import pandas as pd

# 1. Load the dataset
file_name = 'SQL_Sales_Dataset_200_Rows.xlsx'
df = pd.read_excel(file_name)

print("=== TASK 1: Load Dataset & View Info ===")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\n=== TASK 2: Handle Missing Values & Duplicates ===")
print("Missing values before cleaning:\n", df.isnull().sum())
df = df.drop_duplicates()
df = df.ffill()
print("Data cleaned successfully!")

print("\n=== TASK 3: Group Data & Find Total Revenue by Category ===")
category_revenue = df.groupby('category')['total_price'].sum().reset_index()
print(category_revenue)

print("\n=== TASK 4: Sort Data by Multiple Columns ===")
sorted_df = df.sort_values(by=['category', 'total_price'], ascending=[True, False])
print(sorted_df.head(10))

print("\n=== TASK 5: Correlation Matrix for Numerical Columns ===")
numeric_df = df.select_dtypes(include=['number'])
correlation_matrix = numeric_df.corr()
print(correlation_matrix)
# --- BONUS/ADDITIONAL CHECKS FOR AVERAGE ORDER VALUE & TOP CUSTOMERS ---
print("\n=== EXTRA: Average Order Value & Top Customers ===")
avg_order_value = df['total_price'].mean()
print(f"Average Order Value (AOV): {avg_order_value:.2f}")

top_customers = df.groupby('customer_name')['total_price'].sum().reset_index()
top_customers = top_customers.sort_values(by='total_price', ascending=False).head(5)
print("\nTop 5 Customers by Total Spend:")
print(top_customers)