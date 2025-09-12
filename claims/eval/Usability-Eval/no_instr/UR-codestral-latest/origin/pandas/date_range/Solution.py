import pandas as pd

# Create a DatetimeIndex with a fixed frequency
# Starts from '2021-01-01 00:00:00', ends before '2021-01-02 00:00:00', and has a frequency of 1 hour
index = pd.date_range(start='2021-01-01', end='2021-01-02', freq='H')

# Print the DatetimeIndex
print(index)
