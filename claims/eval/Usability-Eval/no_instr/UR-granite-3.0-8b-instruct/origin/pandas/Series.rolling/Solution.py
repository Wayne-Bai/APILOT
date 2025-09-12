import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column for which you want to perform rolling window calculations
window_size = 5  # Change this value as per your requirement

# Calculate rolling mean
df['rolling_mean'] = df['column_name'].rolling(window=window_size).mean()

# Calculate rolling standard deviation
df['rolling_std'] = df['column_name'].rolling(window=window_size).std()

# Calculate rolling sum
df['rolling_sum'] = df['column_name'].rolling(window=window_size).sum()

# Calculate rolling minimum
df['rolling_min'] = df['column_name'].rolling(window=window_size).min()

# Calculate rolling maximum
df['rolling_max'] = df['column_name'].rolling(window_size).max()
