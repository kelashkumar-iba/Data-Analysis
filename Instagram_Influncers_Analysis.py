import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset with specified column names and adjust for spaces and quotes
df = pd.read_csv("D:\\DataCamp\\Datasets\\influncers.csv", skipinitialspace=True, quotechar='"')

# Convert Followers, Authentic engagement, and Engagement avg to numeric
df['Followers'] = df['Followers'].str.replace('M', 'e6').str.replace('K', 'e3').astype(float)
df['Authentic engagement'] = df['"Authentic engagement"'].str.replace('K', 'e3').astype(float)
df['Engagement avg'] = df['"Engagement avg"'].str.replace('K', 'e3').astype(float)

# Audience Country and Engagement Average
audience_engagement = df.groupby('Audience country(mostly)')['Engagement avg'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
audience_engagement.plot(kind='bar', color='green')
plt.title('Average Engagement by Audience Country')
plt.xlabel('Audience Country')
plt.ylabel('Engagement Average')
plt.show()
