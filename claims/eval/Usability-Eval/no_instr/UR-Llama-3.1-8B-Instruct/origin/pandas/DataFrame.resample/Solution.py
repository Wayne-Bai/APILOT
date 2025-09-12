# Import the pandas library
import pandas as pd

# Create a sample time-series data
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08'],
    'Value': [10, 15, 20, 25, 30, 35, 40, 45]
}
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Print the original data
print("Original Data:")
print(df)

# Resample the data by day
resampled_df = df.set_index('Date').resample('D').mean()

# Print the resampled data
print("\nResampled Data by Day:")
print(resampled_df)

# Resample the data by week
resampled_df_week = df.set_index('Date').resample('W').mean()

# Print the resampled data by week
print("\nResampled Data by Week:")
print(resampled_df_week)

# Resample the data by month
resampled_df_month = df.set_index('Date').resample('M').mean()

# Print the resampled data by month
print("\nResampled Data by Month:")
print(resampled_df_month)
