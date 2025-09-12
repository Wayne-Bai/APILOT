import pandas as pd

# Import data from a CSV file
df = pd.read_csv('data.csv')

# Set the frequency of the rolling window (e.g. daily, weekly)
freq = 'D'

# Calculate the moving average with a rolling window
df['rolling_mean'] = df['value'].rolling(window=10, freq=freq).mean()
