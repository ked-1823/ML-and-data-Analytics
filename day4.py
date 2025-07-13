import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Grocery', 'Clothing', 'Grocery', 'Electronics'],
    'Product': ['Laptop', 'Shirt', 'Mobile', 'Rice', 'Jeans', 'Milk', 'Tablet'],
    'Price': [70000, 1200, 15000, 800, 1500, 50, 22000],
    'Units_Sold': [120, 300, 500, 1000, 250, 1300, 90]
}

df = pd.DataFrame(data)
print(df)
print("/////////////////////////////////////")

# Filter price > 5000
exp = df[df['Price'] > 5000]
print("Filtered Expensive Products:\n", exp)

# Sort by Price descending
sorted_price = df.sort_values(by='Price', ascending=False)
print("\nPrice in descending order:\n", sorted_price)

# Add revenue column
df['revenue'] = df['Price'] * df['Units_Sold']
print("\nRevenue column added:\n", df)

# Grouped by Category
grouped = df.groupby('Category').agg({
    'Price': 'mean',
    'revenue': 'sum',
    'Product': 'count'
}).rename(columns={'Product': 'Product_Count'})

print("\nGrouped Data:\n", grouped)
print("unit sold >500")
new_df=df[df['Units_Sold']>=500]
print(new_df)

# === Visualizations ===

# Histogram of prices
sns.histplot(df['Price'], bins=10, kde=True)
plt.title('Price Distribution')
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Barplot of average price by category
sns.barplot(x=grouped.index, y=grouped['Price'])
plt.title('Average Price by Category')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

