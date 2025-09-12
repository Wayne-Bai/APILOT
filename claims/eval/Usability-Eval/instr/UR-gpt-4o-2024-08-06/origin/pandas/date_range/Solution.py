import pandas as pd

# Define the start and end dates
start_date = '2023-01-01'
end_date = '2023-01-10'

# Generate a fixed frequency DatetimeIndex with daily frequency
datetime_index = pd.date_range(start=start_date, end=end_date, freq='D')

# Print the resulting DatetimeIndex
print(datetime_index)
