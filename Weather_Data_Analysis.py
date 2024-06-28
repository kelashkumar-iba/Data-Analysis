import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("D:\\DataCamp\\Datasets\\weather.csv")

# Calculate statistics
average_temp = df['Temperature'].mean()
min_temp = df['Temperature'].min()
max_temp = df['Temperature'].max()

# Line plot of temperature variation over time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Temperature'], marker='o', linestyle='-', color='b')
plt.title('Temperature Variation')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
