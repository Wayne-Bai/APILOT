import pandas as pd

# Sample time-series data
data = {
    'date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'value': range(100)
}

# Create a DataFrame
df = pd.DataFrame(data)
df.set_index('date', inplace=True)

# Resample the data to monthly frequency and calculate the mean
resampled_df = df.resample('M').mean()

print(resampled_df)
