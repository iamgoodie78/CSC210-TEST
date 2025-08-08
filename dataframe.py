
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("main.csv")

# Optional: Set a consistent style
plt.style.use('ggplot')

# 1. Bar Plot: Total quantity by fruit
plt.figure(figsize=(10, 6))
total_qty = df.groupby("Fruit")["Quantity"].sum()
total_qty.plot(kind="bar")
plt.title("Total Quantity by Fruit")
plt.ylabel("Quantity")
plt.xlabel("Fruit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Pie Chart: Distribution of fruit types
plt.figure(figsize=(8, 8))
df["Fruit"].value_counts().plot(kind="pie", autopct='%1.1f%%')
plt.title("Fruit Type Distribution")
plt.ylabel("")  # Hide y-label
plt.show()

# 3. Histogram: Quantity distribution
plt.figure(figsize=(10, 6))
plt.hist(df["Quantity"], bins=20, edgecolor='black')
plt.title("Histogram of Quantity")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()

# 4. Box Plot: Quantity by fruit
plt.figure(figsize=(12, 6))
df.boxplot(column="Quantity", by="Fruit")
plt.title("Boxplot of Quantity by Fruit")
plt.suptitle("")  # Hide the default title
plt.xlabel("Fruit")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Scatter Plot: Quantity vs Price
plt.figure(figsize=(10, 6))
plt.scatter(df["Quantity"], df["Price"], alpha=0.6)
plt.title("Scatter Plot: Quantity vs Price")
plt.xlabel("Quantity")
plt.ylabel("Price")
plt.show()

# 6. Line Plot: Average price per fruit
plt.figure(figsize=(10, 6))
avg_price = df.groupby("Fruit")["Price"].mean()
avg_price.plot(kind="line", marker='o')
plt.title("Average Price per Fruit")
plt.xlabel("Fruit")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 7. Horizontal Bar Chart: Average quantity per color
plt.figure(figsize=(10, 6))
avg_qty_color = df.groupby("Color")["Quantity"].mean().sort_values()
avg_qty_color.plot(kind="barh")
plt.title("Average Quantity by Color")
plt.xlabel("Quantity")
plt.ylabel("Color")
plt.tight_layout()
plt.show()

# 8. Area Plot: Cumulative quantity of top 5 fruits
plt.figure(figsize=(10, 6))
top5 = df["Fruit"].value_counts().nlargest(5).index
df_top5 = df[df["Fruit"].isin(top5)]
cum_qty = df_top5.groupby(["Fruit", "ID"])["Quantity"].sum().unstack(0).fillna(0).cumsum()
cum_qty.plot.area()
plt.title("Cumulative Quantity of Top 5 Fruits")
plt.xlabel("ID")
plt.ylabel("Cumulative Quantity")
plt.tight_layout()
plt.show()

# 9. Bar Chart: Count of fruits by color
plt.figure(figsize=(10, 6))
color_counts = df["Color"].value_counts()
color_counts.plot(kind="bar", color='teal')
plt.title("Count of Fruits by Color")
plt.xlabel("Color")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
