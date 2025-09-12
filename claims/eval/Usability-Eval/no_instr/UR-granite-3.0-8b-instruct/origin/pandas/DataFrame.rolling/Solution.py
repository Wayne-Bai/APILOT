import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to perform rolling window calculations on
window_size = 5  # Change this value to the desired window size

# Perform rolling mean calculation
df['rolling_mean'] = df['column_name'].rolling(window=window_size).mean()

# Perform rolling standard deviation calculation
df['rolling_std'] = df['column_name'].rolling(window=window_size).std()

# Perform rolling sum calculation
df['rolling_sum'] = df['column_name'].rolling(window=window_size).sum()

# Perform rolling minimum calculation
df['rolling_min'] = df['column_name'].rolling(window=window_size).min()

# Perform rolling maximum calculation
df['rolling_max'] = df['column_name'].rolling(window=window_size).max()
