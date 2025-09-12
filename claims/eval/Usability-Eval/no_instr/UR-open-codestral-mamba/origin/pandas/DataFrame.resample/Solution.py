import pandas as pd

# Assuming df is your Dataframe and 'date' is your date field and 'value' is the field you want to resample

df['date'] = pd.to_datetime(df['date'])  # convert date to datetime type
df.set_index('date', inplace=True)  # set date as index

# 'value' is your data you want to resample
df['value'] = pd.to_numeric(df['value'])  # ensure that value is numeric

# Resample the data to yearly and get the mean
yearly_mean = df['value'].resample('Y').mean()

print(yearly_mean)
