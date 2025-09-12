# Import necessary library
import pandas as pd

# Create a sample time-series data
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    'Value': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Print the original data
print("Original Data:")
print(df)

# Resample the data with a time frequency of 'D' (daily)
# This will create new rows for each day, even if there is no data
resampled_df = df.set_index('Date').resample('D').mean().reset_index()

# Print the resampled data
print("\nResampled Data (daily mean):")
print(resampled_df)
