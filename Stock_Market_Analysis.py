import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
stocks_df = pd.read_csv("D:\DataCamp\Datasets\stocks.csv")


# Calculate daily returns for the specific stock
stock_symbol = 'Apple_Price'
stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])
stocks_df = stocks_df.sort_values(by='Date')
stocks_df['Apple_Daily_Return'] = stocks_df[stock_symbol].pct_change()

# Sample data to reduce congestion
sampled_data = stocks_df['Apple_Daily_Return'].dropna().sample(100, random_state=42)

# Plot the distribution of daily returns
plt.figure(figsize=(10, 6))
sns.histplot(sampled_data, kde=True, bins=30)
plt.title(f'Distribution of Daily Returns for Apple')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
