import pandas as pd

# Sample time-series data
date_rng = pd.date_range(start='1/1/2020', end='1/15/2020', freq='H')
df = pd.DataFrame(date_rng, columns=['date'])
df['value'] = range(len(date_rng))

# Resampling the data from hourly to daily sum
df.set_index('date', inplace=True)
df_daily = df.resample('D').sum()

print(df_daily)
