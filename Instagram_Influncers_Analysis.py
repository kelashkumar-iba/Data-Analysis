import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset with specified column names and adjust for spaces and quotes
file_path = r"D:\DataCamp\Datasets\influncers.csv"
df = pd.read_csv(file_path, skipinitialspace=True, quotechar='"')

# Display the first few rows of the dataset to verify
print(df.head())

# Convert Followers, Authentic engagement, and Engagement avg to numeric
df['Followers'] = df['Followers'].str.replace('M', 'e6').str.replace('K', 'e3').astype(float)
df['Authentic engagement'] = df['"Authentic engagement\n"'].str.replace('K', 'e3').astype(float)
df['Engagement avg'] = df['"Engagement avg\n"'].str.replace('K', 'e3').astype(float)

# Audience Country and Engagement Average
audience_engagement = df.groupby('Audience country(mostly)')['Engagement avg'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
audience_engagement.plot(kind='bar', color='green')
plt.title('Average Engagement by Audience Country')
plt.xlabel('Audience Country')
plt.ylabel('Engagement Average')
plt.show()
