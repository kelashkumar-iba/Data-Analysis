import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("D:\DataCamp\Datasets\weather.csv")

# Sample the data to avoid congestion (e.g., sample 1000 points)
sampled_df = df.sample(n=1000, random_state=1)

# Histogram of humidity levels (sampled data)
plt.figure(figsize=(8, 6))
plt.hist(sampled_df['Humidity'], bins=20, color='g', alpha=0.7)
plt.title('Humidity Distribution (Sampled Data)')
plt.xlabel('Humidity (%)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Sample the data to avoid congestion (e.g., sample 1000 points)
sampled_df = df.sample(n=1000, random_state=1)

# Box plot of wind speed (sampled data)
plt.figure(figsize=(10, 6))
plt.boxplot(sampled_df['WindSpeed'], vert=False)
plt.title('Wind Speed Distribution (Sampled Data)')
plt.xlabel('Wind Speed (m/s)')
plt.yticks([])
plt.grid(True)
plt.show()

