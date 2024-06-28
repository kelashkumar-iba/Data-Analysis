import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("D:\DataCamp\Datasets\weather.csv")

# Sample the data to avoid congestion (e.g., sample 100 points)
sampled_df = df.sample(n=100, random_state=1)

# Line plot of temperature variation over time (sampled data)
plt.figure(figsize=(12, 6))
plt.plot(sampled_df['Date'], sampled_df['Temperature'], marker='o', linestyle='-', color='b')
plt.title('Temperature Variation (Sampled Data)')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
