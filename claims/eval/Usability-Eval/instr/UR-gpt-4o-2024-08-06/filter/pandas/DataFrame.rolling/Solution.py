import pandas as pd

# Create a sample DataFrame
data = {'values': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}
df = pd.DataFrame(data)

# Define the rolling window size
window_size = 3

# Calculate the rolling mean
df['rolling_mean'] = df['values'].rolling(window=window_size).mean()

# Calculate the rolling sum
df['rolling_sum'] = df['values'].rolling(window=window_size).sum()

# Calculate the rolling standard deviation
df['rolling_std'] = df['values'].rolling(window=window_size).std()

# Output the DataFrame with rolling calculations
print(df)
