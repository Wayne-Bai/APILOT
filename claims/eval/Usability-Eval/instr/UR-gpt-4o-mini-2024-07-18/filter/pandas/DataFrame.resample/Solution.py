import pandas as pd

# Sample time-series data creation
date_rng = pd.date_range(start='2020-01-01', end='2020-01-10', freq='D')
data = pd.DataFrame(date_rng, columns=['date'])
data['data'] = pd.Series(range(1,len(data)+1))

# Set the date as the index
data.set_index('date', inplace=True)

# Resampling the data to a different frequency (e.g., '2D' for every 2 days)
resampled_data = data.resample('2D').mean()

print(resampled_data)
