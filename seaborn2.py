import seaborn as sns
import matplotlib.pyplot as plt

# Imagine this is juice data (in mL) by age
juice_data = {
    'Age': [12, 13, 13, 14, 12, 14, 13],
    'Juice_ml': [200, 150, 220, 180, 210, 160, 170]
}

# Convert to a DataFrame
import pandas as pd
df = pd.DataFrame(juice_data)

# Make a line plot
sns.lineplot(x='Age', y='Juice_ml', data=df)
plt.title('Juice Consumption by Age')
plt.xlabel('Age')
plt.ylabel('Juice (mL)')
plt.show()
