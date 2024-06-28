import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("D:\DataCamp\Datasets\weather.csv")

# Summarize total precipitation by station
total_precipitation = df.groupby('Station')['Precipitation'].sum().sort_values(ascending=False).head(10)

# Bar chart of precipitation by top 10 stations
plt.figure(figsize=(10, 6))
total_precipitation.plot(kind='bar', color='b')
plt.title('Total Precipitation by Top 10 Stations')
plt.xlabel('Station')
plt.ylabel('Total Precipitation')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
