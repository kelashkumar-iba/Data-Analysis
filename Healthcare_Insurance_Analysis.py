import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
healthcare = pd.read_csv("D:\\DataCamp\\Datasets\\insurance.csv")

# Set the style for the plots
sns.set(style="whitegrid")

# Plot the distribution of ages
plt.figure(figsize=(10, 6))
sns.histplot(healthcare['age'], kde=True, bins=20)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# Plot the relationship between BMI and charges
plt.figure(figsize=(10, 6))
sns.scatterplot(x='bmi', y='charges', data=healthcare)
plt.title('BMI vs. Charges')
plt.xlabel('BMI')
plt.ylabel('Charges')
plt.show()


# Plot charges for smokers vs non-smokers
plt.figure(figsize=(10, 6))
sns.boxplot(x='smoker', y='charges', data=healthcare)
plt.title('Charges for Smokers vs. Non-Smokers')
plt.xlabel('Smoker')
plt.ylabel('Charges')
plt.show()


# Plot charges across different regions
plt.figure(figsize=(10, 6))
sns.boxplot(x='region', y='charges', data=healthcare)
plt.title('Charges by Region')
plt.xlabel('Region')
plt.ylabel('Charges')
plt.show()


# Create age groups
healthcare['age_group'] = pd.cut(healthcare['age'], bins=[18, 30, 40, 50, 60, 70], labels=['18-29', '30-39', '40-49', '50-59', '60-69'])

# Plot average charges by age group
plt.figure(figsize=(10, 6))
sns.barplot(x='age_group', y='charges', data=healthcare, estimator=lambda x: sum(x) / len(x))
plt.title('Average Charges by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Charges')
plt.show()

