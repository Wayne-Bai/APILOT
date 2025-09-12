import pandas as pd

# Sample data
data = {
    'date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}

df = pd.DataFrame(data)

# Set 'date' as the index
df.set_index('date', inplace=True)

# Perform rolling window calculations
df['rolling_mean'] = df['value'].rolling(window=3).mean()
df['rolling_sum'] = df['value'].rolling(window=3).sum()
df['rolling_std'] = df['value'].rolling(window=3).std()

print(df)
