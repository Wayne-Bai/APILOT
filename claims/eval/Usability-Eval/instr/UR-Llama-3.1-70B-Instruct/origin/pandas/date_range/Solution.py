# Importing the pandas library
import pandas as pd
import numpy as np

# Specify the start and end dates
start_date = '2022-01-01'
end_date = '2022-01-31'

# Generate a fixed frequency DatetimeIndex with daily frequency
date_index = pd.date_range(start=start_date, end=end_date, freq='D')

# Print the DatetimeIndex
print(date_index)

# Generate a fixed frequency DatetimeIndex with business day frequency
date_index_business_days = pd.date_range(start=start_date, end=end_date, freq='B')

# Print the DatetimeIndex
print(date_index_business_days)

# Generate a fixed frequency DatetimeIndex with hourly frequency
date_index_hourly = pd.date_range(start=start_date, end=end_date, freq='H')

# Print the DatetimeIndex
print(date_index_hourly)
