import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
stocks_df = pd.read_csv("D:\DataCamp\Datasets\stocks.csv")

# Calculate average closing price and standard deviation (volatility) for each stock
average_closing_price = stocks_df[price_columns].mean()
volatility = stocks_df[price_columns].std()

# Create a figure and axes
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot average closing price
color = 'tab:blue'
ax1.set_xlabel('Stock Symbol')
ax1.set_ylabel('Average Closing Price', color=color)
ax1.bar(average_closing_price.index, average_closing_price.values, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.xticks(rotation=45)

# Plot volatility on the same axis
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Volatility', color=color)
ax2.plot(average_closing_price.index, volatility.values, color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Average Closing Price and Volatility for Different Stocks')
plt.grid(True)
plt.show()
