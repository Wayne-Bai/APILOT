import pandas as pd

# Sample data creation
data = {'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
        'value': [5, 6, 7, 8, 9]}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

# Set the date column as the index
df.set_index('date', inplace=True)

# Resampling the data to find the mean for '2 days'
resampled_data = df.groupby(pd.Grouper(freq='2D')).mean()

print(resampled_data)
