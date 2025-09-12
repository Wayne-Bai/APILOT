# Import the pandas library
import pandas as pd

# Import numpy for date range generation
import numpy as np

# Generate a sample time-series data
date_range = pd.date_range(start='2022-01-01', end='2022-01-10', freq='H')
values = np.random.rand(len(date_range))
data = pd.Series(values, index=date_range)

# Print original data
print("Original Data:")
print(data.head())

# Resample data to daily frequency and calculate mean
resampled_data = data.resample('D').mean()

# Print resampled data
print("\nResampled Data (Daily Mean):")
print(resampled_data)

# Resample data to weekly frequency and calculate sum
resampled_dataWeekly = data.resample('W').sum()

# Print resampled data
print("\nResampled Data (Weekly Sum):")
print(resampled_dataWeekly)
