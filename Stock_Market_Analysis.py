import pandas as pd 

stocks_df = pd.read_csv("D:\DataCamp\Datasets\stocks.csv")
print(stocks_df.head())

import matplotlib.pyplot as plt
import seaborn as sns

# Filter data for a specific stock (e.g., 'AAPL')
stock_symbol = 'AAPL'
stock_data = stocks_df[stocks_df['symbol'] == stock_symbol]

# Plot closing prices over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=stock_data, x='date', y='close')
plt.title(f'Trend of Closing Prices for {stock_symbol}')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
