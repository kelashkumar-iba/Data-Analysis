import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Load the dataset
stocks_df = pd.read_csv("D:\\DataCamp\\Datasets\\stocks.csv")

# Plot the trend of Natural Gas Prices over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Natural_Gas_Price', data=stocks_df)
plt.title('Trend of Natural Gas Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Natural Gas Price')
plt.xticks(rotation=45)
plt.show()
