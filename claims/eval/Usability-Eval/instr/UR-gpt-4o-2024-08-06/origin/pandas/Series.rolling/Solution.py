import pandas as pd

# Sample data
data = {
    'value': [10, 14, 18, 22, 26, 30, 34, 38, 42, 46]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the rolling window size
window_size = 3

# Calculate the rolling mean
df['rolling_mean'] = df['value'].rolling(window=window_size).mean()

# Calculate the rolling sum
df['rolling_sum'] = df['value'].rolling(window=window_size).sum()

# Calculate the rolling maximum
df['rolling_max'] = df['value'].rolling(window=window_size).max()

# Calculate the rolling minimum
df['rolling_min'] = df['value'].rolling(window=window_size).min()

print(df)
