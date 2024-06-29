import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
stocks_df = pd.read_csv("D:\DataCamp\Datasets\stocks.csv")

# Filter data for a specific stock (e.g., 'Apple')
stock_symbol = 'Apple_Price'
stock_data = stocks_df[['Date', stock_symbol]]

# Sample data to reduce congestion
stock_data = stock_data.sample(50, random_state=42).sort_values('Date')

# Plot closing prices over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=stock_data, x='Date', y=stock_symbol)
plt.title(f'Trend of Closing Prices for Apple')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# Select columns for closing prices
price_columns = [
    'Natural_Gas_Price', 'Crude_oil_Price', 'Copper_Price', 'Bitcoin_Price', 'Platinum_Price', 
    'Ethereum_Price', 'S&P_500_Price', 'Nasdaq_100_Price', 'Apple_Price', 'Tesla_Price', 
    'Microsoft_Price', 'Silver_Price', 'Google_Price', 'Nvidia_Price', 'Berkshire_Price', 
    'Netflix_Price', 'Amazon_Price', 'Meta_Price', 'Gold_Price'
]

# Calculate the correlation matrix
correlation_matrix = stocks_df[price_columns].corr()

# Plot the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Between Closing Prices of Different Stocks')
plt.show()
