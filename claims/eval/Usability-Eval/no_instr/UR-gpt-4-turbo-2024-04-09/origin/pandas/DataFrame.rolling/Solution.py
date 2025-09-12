import pandas as pd

# Create a sample DataFrame
data = {
    'date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'value': [i**2 for i in range(10)]  # square numbers for example
}

df = pd.DataFrame(data)

# Calculate a rolling window calculation of the 'value' column
# Here using a window size of 3 and calculating the mean
df['rolling_mean'] = df['value'].rolling(window=3).mean()

# Display the DataFrame to see the rolling mean results
print(df)
