import pandas as pd

# Create a sample time-series data frame
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='H')
data = {'value': range(len(date_rng))}
df = pd.DataFrame(data, index=date_rng)

# Resample the data to daily frequency and calculate the mean
resampled_df = df.resample('D').mean()

print(resampled_df)
