import pandas as pd

# Assuming you have a DataFrame called 'df' with a DateTimeIndex
df = pd.DataFrame({'value': [1, 2, 3, 4, 5]}, index=pd.date_range('2022-01-01', periods=5))

# Resample the data to daily values
resampled_df = df.resample('D').mean()

print(resampled_df)
