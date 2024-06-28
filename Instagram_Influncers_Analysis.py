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

# Relationship between Followers and Authentic Engagement
plt.figure(figsize=(10, 6))
plt.scatter(df['Followers'], df['Authentic engagement'], color='blue')
plt.title('Followers vs Authentic Engagement')
plt.xlabel('Followers')
plt.ylabel('Authentic Engagement')
for i, txt in enumerate(df['Influencer insta name']):
    plt.annotate(txt, (df['Followers'][i], df['Authentic engagement'][i]))
plt.grid(True)
plt.show()