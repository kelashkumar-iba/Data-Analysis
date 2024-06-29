import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
stocks_df = pd.read_csv("D:\DataCamp\Datasets\stocks.csv")

# Select columns for volumes
volume_columns = [
    'Natural_Gas_Vol.', 'Crude_oil_Vol.', 'Copper_Vol.', 'Bitcoin_Vol.', 'Platinum_Vol.', 
    'Ethereum_Vol.', 'Nasdaq_100_Vol.', 'Apple_Vol.', 'Tesla_Vol.', 'Microsoft_Vol.', 
    'Silver_Vol.', 'Google_Vol.', 'Nvidia_Vol.', 'Berkshire_Vol.', 'Netflix_Vol.', 
    'Amazon_Vol.', 'Meta_Vol.', 'Gold_Vol.'
]

# Melt the dataframe to have a long format for seaborn plotting
volume_data = stocks_df.melt(id_vars='Date', value_vars=volume_columns, var_name='Stock', value_name='Volume')

# Sample data to reduce congestion
volume_data = volume_data.sample(frac=0.1, random_state=42)

# Plot volume traded over time for different stocks
plt.figure(figsize=(14, 8))
sns.lineplot(data=volume_data, x='Date', y='Volume', hue='Stock')
plt.title('Volume Traded Over Time for Different Stocks')
plt.xlabel('Date')
plt.ylabel('Volume Traded')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
