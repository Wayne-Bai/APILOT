import pandas as pd

# Sample data. Replace this with your real data.
data = pd.DataFrame({
    'Date': pd.date_range(start='2021-01-01', periods=10, freq='M'),
    'Value': [10, 15, 13, 19, 20, 17, 22, 25, 24, 21]
})

# Create a DataFrame with a rolling mean and std
data['Rolling Mean'] = data['Value'].rolling(window=3).mean()
data['Rolling Std'] = data['Value'].rolling(window=3).std()

print(data)
