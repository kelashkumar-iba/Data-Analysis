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
