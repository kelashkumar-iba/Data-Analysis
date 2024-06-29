import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
stocks_df = pd.read_csv("D:\DataCamp\Datasets\stocks.csv")

# Filter data for a specific stock (e.g., 'Apple')
stock_symbol = 'Apple_Price'
stock_data = stocks_df[['Date', stock_symbol]]

# Plot closing prices over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=stock_data, x='Date', y=stock_symbol)
plt.title(f'Trend of Closing Prices for Apple')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
