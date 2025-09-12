import pandas as pd

# Sample time-series data creation
date_range = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
data = pd.Series(range(len(date_range)), index=date_range)

# Resampling the time-series data to a different frequency (e.g., every 2 days)
resampled_data = data.resample('2D').sum()

print(resampled_data)
