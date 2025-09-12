import pandas as pd

# Example data
data = {
    'date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'value': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
}

# Create DataFrame
df = pd.DataFrame(data)

# Setting 'date' column as index
df.set_index('date', inplace=True)

# Calculate rolling window mean with a window size of 3
df['rolling_mean'] = df['value'].rolling(window=3).mean()

# Calculate rolling window sum with a window size of 3
df['rolling_sum'] = df['value'].rolling(window=3).sum()

# Display DataFrame with rolling calculations
print(df)
