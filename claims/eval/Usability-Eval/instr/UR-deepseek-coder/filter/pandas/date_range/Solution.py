import pandas as pd

# Define the start and end dates
start_date = '2023-01-01'
end_date = '2023-12-31'

# Define the frequency (e.g., 'D' for daily, 'M' for monthly)
frequency = 'D'

# Generate the DatetimeIndex with the specified frequency
datetime_index = pd.date_range(start=start_date, end=end_date, freq=frequency)

# Display the resulting DatetimeIndex
print(datetime_index)
