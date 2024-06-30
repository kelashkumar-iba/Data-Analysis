import pandas as pd
import plotly.express as px

# Load the dataset
file_path = r'D:\DataCamp\Datasets\stocks.csv'
stocks_df = pd.read_csv(file_path)

# Filter data for two specific stocks (e.g., 'Apple' and 'Tesla')
volume_columns = ['Date', 'Apple_Vol.', 'Tesla_Vol.']
volume_data = stocks_df[volume_columns].dropna()

# Convert Date to datetime format
volume_data['Date'] = pd.to_datetime(volume_data['Date'], format='%d-%m-%Y')

# Sample data to reduce congestion
volume_data = volume_data.sample(100, random_state=42).sort_values('Date')

# Plot volume traded over time for both stocks
fig = px.line(volume_data, x='Date', y=['Apple_Vol.', 'Tesla_Vol.'], title='Volume Traded Comparison Between Apple and Tesla')
fig.update_layout(xaxis_title='Date', yaxis_title='Volume Traded', xaxis=dict(tickangle=-45))
fig.show()
