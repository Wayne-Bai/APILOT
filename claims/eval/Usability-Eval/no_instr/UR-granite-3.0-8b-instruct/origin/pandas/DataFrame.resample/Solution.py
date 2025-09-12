import pandas as pd

# Assuming df is your DataFrame and 'date' is the column containing dates
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Resample data to a daily frequency
daily_data = df.resample('D').mean()

# Resample data to a monthly frequency
monthly_data = df.resample('M').mean()

# Resample data to a yearly frequency
yearly_data = df.resample('Y').mean()
