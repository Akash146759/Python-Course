import pandas as pd
import sqlite3

# Step 1: Read CSV file
df = pd.read_csv("Weather Dataset.xlsx")

# Step 2: Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("weather.db")

# Step 3: Write data to a table named 'weather'
df.to_sql("weather", conn, if_exists="replace", index=False)

# Step 4: Close the connection
conn.close()

print("✅ Data imported successfully into 'weather.db'")
