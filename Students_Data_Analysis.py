import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
students_df = pd.read_csv("D:\DataCamp\Datasets\students.csv")

# Calculate average scores in each subject by student ID
student_performance = students_df.groupby('ID')[['Algebra', 'Calculus1', 'Calculus2', 'Statistics', 'Probability', 'Measure', 'Functional_analysis']].mean()

# Randomly select 7 student IDs
random_students = np.random.choice(student_performance.index, size=7, replace=False)

# Filter the dataframe for randomly selected students
student_performance_random = student_performance.loc[random_students]

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(14, 8))

# Define professional colors manually from a colormap
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Plot the data with specified colors
student_performance_random.plot(kind='bar', ax=ax, color=colors)

# Set plot title and labels
plt.title('Average Scores in Different Subjects by Randomly Selected 7 Students')
plt.xlabel('Student ID')
plt.ylabel('Average Score')

# Rotate x-ticks for better readability
plt.xticks(rotation=45, ha='right')

plt.show()
