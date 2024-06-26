# Task 1: Plotting Total Homeless Individuals and Family Members by Region
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:\\Users\\Kelash Kumar\\Downloads\\homelessness.csv"
df = pd.read_csv(file_path)

# Calculate total individuals and family members by region
region_data = df.groupby('region')[['individuals', 'family_members']].sum()

# Plotting
region_data.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Distribution of Homeless Individuals and Family Members by Region')
plt.xlabel('Region')
plt.ylabel('Number of People')
plt.xticks(rotation=45)
plt.legend(['Individuals', 'Family Members'])
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# ----------------------------------------------------------------

# Task 2: Bar Chart of Homeless Individuals by State Population
# Calculate homeless individuals per 100,000 state population
df['homeless_per_100k'] = (df['individuals'] / df['state_pop']) * 100000

# Plotting
plt.figure(figsize=(12, 8))
plt.bar(df['state'], df['homeless_per_100k'], color='orange')
plt.title('Homeless Individuals per 100,000 State Population')
plt.xlabel('State')
plt.ylabel('Homeless Individuals per 100,000 Population')
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

