import pandas as pd

# Sample data
data = {
    'date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'value': [1, 3, 5, 2, 4, 6, 9, 5, 7, 11]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the 'date' column as the index
df.set_index('date', inplace=True)

# Calculate rolling window calculations with a window size of 3
rolling_mean = df['value'].rolling(window=3).mean()
rolling_sum = df['value'].rolling(window=3).sum()
rolling_std = df['value'].rolling(window=3).std()

# Output the results
print("Original DataFrame:")
print(df)
print("\nRolling Mean (window=3):")
print(rolling_mean)
print("\nRolling Sum (window=3):")
print(rolling_sum)
print("\nRolling Standard Deviation (window=3):")
print(rolling_std)
