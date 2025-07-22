import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('penguins_size.csv')

# Clean data
df = df.dropna()

# Set style
sns.set(style='whitegrid')

# 1️⃣ Stacked Bar: Gender Count per Species
species_sex = df.groupby(['species', 'sex']).size().unstack()
species_sex.plot(kind='bar', stacked=True, figsize=(8, 5), colormap='Pastel1')
plt.title('Gender Distribution Across Species')
plt.ylabel('Count')
plt.xlabel('Species')
plt.legend(title='Sex')
plt.tight_layout()
plt.show()

# 2️⃣ KDE Plot: Flipper Length Distribution by Species
plt.figure(figsize=(8, 5))
for species in df['species'].unique():
    subset = df[df['species'] == species]
    sns.kdeplot(subset['flipper_length_mm'], label=species, fill=True)
plt.title('Flipper Length Density by Species')
plt.xlabel('Flipper Length (mm)')
plt.legend()
plt.show()

# 3️⃣ Swarm Plot: Body Mass vs Species by Sex
plt.figure(figsize=(8, 5))
sns.swarmplot(data=df, x='species', y='body_mass_g', hue='sex', palette='coolwarm')
plt.title('Body Mass Across Species by Sex')
plt.ylabel('Body Mass (g)')
plt.xlabel('Species')
plt.legend(title='Sex')
plt.show()

# 4️⃣ Ridgeline Style Violin Plot: Culmen Length by Island
plt.figure(figsize=(8, 6))
sns.violinplot(data=df, x='island', y='culmen_length_mm', hue='species', split=True, palette='Set3')
plt.title('Culmen Length by Island and Species')
plt.ylabel('Culmen Length (mm)')
plt.xlabel('Island')
plt.legend(title='Species')
plt.show()

# 5️⃣ Heatmap of Grouped Mean Feature Values
group_means = df.groupby('species')[['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']].mean()
plt.figure(figsize=(8, 5))
sns.heatmap(group_means.T, annot=True, fmt=".1f", cmap='YlGnBu')
plt.title('Mean Measurements per Species')
plt.xlabel('Species')
plt.ylabel('Measurement')
plt.show()

# 6️⃣ Custom Highlight: Gentoo Penguins Mass vs Flipper Length
gentoo = df[df['species'] == 'Gentoo']
plt.figure(figsize=(8, 5))
sns.scatterplot(data=gentoo, x='flipper_length_mm', y='body_mass_g', hue='sex', style='sex', s=100, palette='Dark2')
plt.title('Gentoo Penguins: Mass vs Flipper Length')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.show()

# 7️⃣ Fun Fact Bonus: Penguin Size Bubble Plot
plt.figure(figsize=(9, 6))
size_map = {'Adelie': 100, 'Chinstrap': 150, 'Gentoo': 200}
df['bubble_size'] = df['species'].map(size_map)
sns.scatterplot(data=df, x='culmen_length_mm', y='culmen_depth_mm',
                size='bubble_size', hue='species', alpha=0.6, palette='pastel', sizes=(40, 200))
plt.title('Bubble Plot: Culmen Features by Species')
plt.xlabel('Culmen Length (mm)')
plt.ylabel('Culmen Depth (mm)')
plt.legend(title='Species')
plt.show()