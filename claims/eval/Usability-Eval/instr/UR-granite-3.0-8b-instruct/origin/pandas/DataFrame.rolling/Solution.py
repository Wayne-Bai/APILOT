import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to perform rolling calculations on
window_size = 5  # Change this value to the desired window size

df['rolling_mean'] = df['column_name'].rolling(window_size).mean()
df['rolling_std'] = df['column_name'].rolling(window_size).std()
df['rolling_max'] = df['column_name'].rolling(window_size).max()
df['rolling_min'] = df['column_name'].rolling(window_size).min()
