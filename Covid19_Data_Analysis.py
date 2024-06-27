import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import statsmodels.api as sm

# Load the dataset
df = pd.read_csv("D:\\DataCamp\\Datasets\\countrywise.csv")

# Filter out rows with missing values in 'New cases' and 'New deaths'
df_clean = df.dropna(subset=['New cases', 'New deaths'])

# Create scatter plot
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df_clean, x='New cases', y='New deaths', hue='WHO Region', palette='Set2', alpha=0.9)

# Fit and plot trendline
x = df_clean['New cases']
y = df_clean['New deaths']
X = sm.add_constant(x)
model = sm.OLS(y, X)
results = model.fit()
intercept, slope = results.params

plt.plot(x, intercept + slope * x, color='black', linestyle='-', linewidth=2, label=f'Trendline: New Deaths = {intercept:.2f} + {slope:.2f} * New Cases')

# Customize labels and title
plt.title('New Cases vs New Deaths')
plt.xlabel('New Cases')
plt.ylabel('New Deaths')
plt.legend()

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()
