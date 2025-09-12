
import pandas as pd

# Create a sample dataframe with datetime index
df = pd.DataFrame({'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
                   'value': [1, 2, 3, 4, 5]})
df.index = pd.to_datetime(df['date'])

# Resample data to daily frequency using the mean method
daily_mean = df.resample('D', on='date').mean()
print(daily_mean)
