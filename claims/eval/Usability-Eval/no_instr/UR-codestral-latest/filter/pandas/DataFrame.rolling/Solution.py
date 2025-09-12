import pandas as pd
import numpy as np

# Assuming df is your DataFrame and 'column_name' is the column you want to calculate the rolling window for

# Create a rolling window object
window_size = 3  # replace with your desired window size
rolling = df['column_name'].rolling(window=window_size)

# Calculate the mean
df['rolling_mean'] = rolling.mean()

# Calculate the standard deviation
df['rolling_std'] = rolling.std()

# Calculate the minimum
df['rolling_min'] = rolling.min()

# Calculate the maximum
df['rolling_max'] = rolling.max()
