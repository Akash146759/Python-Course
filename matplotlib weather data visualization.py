import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_excel("Weather Dataset.xlsx")

# Safely convert Excel date format to datetime if needed
if df['date_time'].dtype != 'datetime64[ns]':
    df['date_time'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df['date_time'], unit='D')

# Set Seaborn theme
sns.set_style("whitegrid")

# ——— 1. Temperature and Humidity Over Time ———
plt.figure(figsize=(14, 5))
sns.lineplot(data=df, x='date_time', y='temperature', label='Temperature (K)', color='orangered')
sns.lineplot(data=df, x='date_time', y='humidity', label='Humidity (%)', color='steelblue')
plt.title("Temperature and Humidity Over Time")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ——— 2. Visibility Distribution ———
plt.figure(figsize=(10, 4))
sns.histplot(df['visibility_in_miles'], bins=30, kde=True, color='teal')
plt.title("Visibility Distribution")
plt.xlabel("Visibility in Miles")
plt.tight_layout()
plt.show()

# ——— 3. Average Temperature by Weather Type ———
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='weather_type', y='temperature', estimator='mean', palette='coolwarm', errorbar=None)
plt.title("Average Temperature by Weather Type")
plt.xlabel("Weather Type")
plt.ylabel("Avg Temperature (K)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ——— 4. Wind Speed vs Wind Direction by Weather Type ———
plt.figure(figsize=(12, 5))
sns.scatterplot(data=df, x='wind_direction', y='wind_speed', hue='weather_type', palette='Set2')
plt.title("Wind Speed vs Wind Direction")
plt.xlabel("Wind Direction (°)")
plt.ylabel("Wind Speed")
plt.tight_layout()
plt.show()

# ——— 5. Air Pollution Boxplot by Weather Description ———
plt.figure(figsize=(16, 5))
top_descriptions = df['weather_description'].value_counts().nlargest(10).index
filtered_df = df[df['weather_description'].isin(top_descriptions)]
sns.boxplot(data=filtered_df, x='weather_description', y='air_pollution_index', palette='viridis')
plt.title("Air Pollution Across Top Weather Descriptions")
plt.xlabel("Weather Description")
plt.ylabel("Air Pollution Index")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# ——— 6. Pairplot of Selected Metrics ———
subset = df[['temperature', 'humidity', 'dew_point', 'air_pollution_index']]
sns.pairplot(subset)
plt.suptitle("Pairplot of Weather Metrics", y=1.02)
plt.show()
