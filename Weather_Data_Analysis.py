import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("D:\DataCamp\Datasets\\weather.csv")


# Count occurrences of each weather condition
weather_counts = df['WeatherCondition'].value_counts().head(10)

# Pie chart of top 10 weather condition frequencies
plt.figure(figsize=(10, 5))
plt.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Top 10 Weather Condition Distribution')
plt.axis('equal')
plt.show()


# Sample the data to avoid congestion (e.g., sample 1000 points)
sampled_df = df.sample(n=1000, random_state=1)

# Histogram of humidity levels (sampled data)
plt.figure(figsize=(10, 5))
plt.hist(sampled_df['Humidity'], bins=20, color='r', alpha=0.7)
plt.title('Humidity Distribution (Sampled Data)')
plt.xlabel('Humidity (%)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Summarize total precipitation by station
total_precipitation = df.groupby('Station')['Precipitation'].sum().sort_values(ascending=False).head(10)

# Bar chart of precipitation by top 10 stations
plt.figure(figsize=(10, 5))
total_precipitation.plot(kind='bar', color='b')
plt.title('Total Precipitation by Top 10 Stations')
plt.xlabel('Station')
plt.ylabel('Total Precipitation')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


df = pd.read_csv("D:\DataCamp\Datasets\weather.csv", parse_dates=['Date'])

# Sample the data to avoid congestion (e.g., sample 100 points)
sampled_df = df.sample(n=100, random_state=1).sort_values(by='Date')

# Line plot of temperature variation over time (sampled data)
plt.figure(figsize=(10, 5))
plt.plot(sampled_df['Date'], sampled_df['Temperature'], marker='o', linestyle='-', color='b')
plt.title('Temperature Variation (Sampled Data)')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.xticks(ticks=sampled_df['Date'][::10], labels=sampled_df['Date'][::10].dt.strftime('%Y-%m-%d'))
plt.grid(True)
plt.show()
