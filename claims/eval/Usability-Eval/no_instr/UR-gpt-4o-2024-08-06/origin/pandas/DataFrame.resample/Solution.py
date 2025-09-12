import pandas as pd

# Sample time-series data
data = {
    'Date': [
        '2023-01-01 00:00:00',
        '2023-01-01 01:00:00',
        '2023-01-01 02:00:00',
        '2023-01-01 03:00:00',
        '2023-01-01 04:00:00',
    ],
    'Value': [100, 150, 200, 250, 300]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as the index
df.set_index('Date', inplace=True)

# Resample the data to 2-hour frequency and calculate the mean
resampled_df = df.resample('2H').mean()

print(resampled_df)
