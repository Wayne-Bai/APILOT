import pandas as pd

# Sample DataFrame with a time-series index
data = {
    'date': ['2023-01-01 12:00', '2023-01-01 13:00', '2023-01-01 14:00', '2023-01-01 15:00'],
    'value': [10, 20, 30, 40]
}

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Resample the data to a different frequency, aggregating with the mean
resampled_df = df.resample('2H').mean()

print(resampled_df)
