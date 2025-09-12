
import pandas as pd

# Create a datetime index with some sample data
date_rng = pd.date_range(start='2022-01-01', end='2022-01-31', freq='D')
df = pd.DataFrame(date_rng, columns=['date'])
df['data'] = [i for i in range(len(df))]

# Convert the index to DatetimeIndex
df.set_index('date', inplace=True)

# Resample the time-series data to a weekly frequency ('W') and calculate the mean of the values in each week
weekly_resampled = df.resample('W').mean()

print(weekly_resampled)
