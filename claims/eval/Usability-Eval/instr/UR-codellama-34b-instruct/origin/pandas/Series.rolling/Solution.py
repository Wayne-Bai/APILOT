
import pandas as pd

# create a sample time series data frame
df = pd.DataFrame({'date': ['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04', '2019-01-05'],
                   'value': [1, 2, 3, 4, 5]})

# convert the date column to a datetime format
df['date'] = pd.to_datetime(df['date'])

# calculate the rolling mean for the last 3 days
df['rolling_mean'] = df['value'].rolling(window=3).mean()

print(df)
