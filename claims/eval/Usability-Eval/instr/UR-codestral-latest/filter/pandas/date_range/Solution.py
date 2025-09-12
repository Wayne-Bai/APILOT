import pandas as pd

# Define the start and end dates
start_date = '2022-01-01'
end_date = '2022-01-10'

# Create the DatetimeIndex
dates = pd.date_range(start=start_date, end=end_date, freq='D')

# Print the DatetimeIndex
print(dates)
