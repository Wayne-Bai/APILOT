# Import necessary libraries
import pandas as pd
import numpy as np

# Generate sample time-series data
np.random.seed(0)
data = np.random.rand(100)

# Create a DateTimeIndex with a frequency of 1 minute
index = pd.date_range('2022-01-01', periods=100, freq='min')

# Create a pandas DataFrame
df = pd.DataFrame(data, index=index, columns=['Value'])

# Resample data to 15-minute intervals and calculate the mean
resampled_df = df['Value'].resample('15min').mean()

print(resampled_df)

# Resample data to daily intervals and calculate the sum
resampled_daily_df = df['Value'].resample('D').sum()

print(resampled_daily_df)

# Resample data to weekly intervals and calculate the max
resampled_weekly_df = df['Value'].resample('W').max()

print(resampled_weekly_df)
