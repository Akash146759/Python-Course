import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Optional: Set Seaborn style
sns.set(style="whitegrid")

# 🌟 Load your dataset
df = pd.read_csv('house_rent.csv')

# 🧹 Clean missing values
df.dropna(inplace=True)

# 📈 Distribution of Rent
sns.histplot(data=df, x='Rent', bins=30, kde=True)
plt.title('Rent Distribution')
plt.show()

# 🧱 Rent variation by city
sns.boxplot(x='City', y='Rent', data=df)
plt.title('Rent by City')
plt.xticks(rotation=45)
plt.show()

# 🚿 Impact of Bathrooms on Rent
sns.barplot(x='Bathroom', y='Rent', data=df)
plt.title('Bathroom Count vs Rent')
plt.show()

# 🏠 BHK vs Rent
sns.violinplot(x='BHK', y='Rent', data=df)
plt.title('BHK vs Rent (Violin Plot)')
plt.show()

# 🔁 Correlation heatmap (numerical features only)
numeric_cols = df.select_dtypes(include=['int64', 'float64'])
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# 📐 Relationship between Size and Rent
sns.regplot(x='Size', y='Rent', data=df)
plt.title('Size vs Rent (Regression Line)')
plt.show()
