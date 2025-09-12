import pandas as pd

# Assuming df is your DataFrame and window_size is the size of the rolling window
df['rolling_mean'] = df['column_name'].rolling(window_size).mean()
df['rolling_std'] = df['column_name'].rolling(window_size).std()
df['rolling_var'] = df['column_name'].rolling(window_size).var()
df['rolling_cov'] = df['column_name'].rolling(window_size).cov()
df['rolling_corr'] = df['column_name'].rolling(window_size).corr()
