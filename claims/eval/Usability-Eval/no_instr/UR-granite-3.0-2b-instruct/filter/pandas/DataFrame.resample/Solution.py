import pandas as pd

# Assuming df is your DataFrame and 'date' and 'value' are columns
df = pd.DataFrame({
    'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    'value': [1, 2, 3, 4, 5]
})
df['date'] = pd.to_datetime(df['date'])

# Resample the data to a new DataFrame with a frequency of 'H' (hourly)
resampled_df = df.resample('H').mean()

print(resampled_df)
