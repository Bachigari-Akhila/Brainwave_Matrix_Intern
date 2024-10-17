import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Simulating the Sales Data
np.random.seed(0)

dates = pd.date_range(start="2023-01-01", end="2023-12-31", periods=1000)
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
quantities = np.random.randint(1, 10, size=1000)
prices = {'Product A': 10, 'Product B': 15, 'Product C': 20, 'Product D': 25, 'Product E': 30}
customers = np.random.randint(100, 200, size=1000)

data = {
    'Date': dates,
    'Product': np.random.choice(products, size=1000),
    'Quantity Sold': quantities,
    'Customer ID': customers
}

sales_df = pd.DataFrame(data)
sales_df['Unit Price'] = sales_df['Product'].map(prices)
sales_df['Total Sale'] = sales_df['Quantity Sold'] * sales_df['Unit Price']

# Step 2: Key Metrics Calculation
total_revenue = sales_df['Total Sale'].sum()
average_sales_per_transaction = sales_df['Total Sale'].mean()
total_units_sold = sales_df['Quantity Sold'].sum()
total_transactions = sales_df.shape[0]

# Step 3: Best-Selling Products
product_sales = sales_df.groupby('Product').agg({
    'Quantity Sold': 'sum',
    'Total Sale': 'sum'
}).sort_values(by='Total Sale', ascending=False)

# Step 4: Sales by Month
sales_df['Month'] = sales_df['Date'].dt.to_period('M')
monthly_sales = sales_df.groupby('Month').agg({'Total Sale': 'sum'}).sort_index()

# Step 5: Customer Analysis
unique_customers = sales_df['Customer ID'].nunique()
avg_transactions_per_customer = sales_df.groupby('Customer ID').size().mean()

# Step 6: Visualization of Sales Data
# a. Monthly Sales Trend
plt.figure(figsize=(10,6))
plt.plot(monthly_sales.index.astype(str), monthly_sales['Total Sale'], marker='o', color='b')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# b. Top-Selling Products
product_sales.plot(kind='bar', y='Total Sale', legend=False, title='Top-Selling Products')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.show()

# Summary of the Analysis
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Average Sales per Transaction: ${average_sales_per_transaction:.2f}")
print(f"Total Units Sold: {total_units_sold}")
print(f"Total Transactions: {total_transactions}")
print(f"Unique Customers: {unique_customers}")
print(f"Average Transactions per Customer: {avg_transactions_per_customer:.2f}")

print("\nBest-Selling Products:")
print(product_sales)
