import pandas as pd

# Assuming you have a DataFrame named 'df' with a datetime index 'date' and a column 'value'
df = pd.DataFrame({
    'date': pd.date_range(start='1/1/2020', end='1/10/2020'),
    'value': range(10)
})
df.set_index('date', inplace=True)

# Resample data to 'M' (Month-end frequency)
df_resampled = df.resample('M').mean()

print(df_resampled)
