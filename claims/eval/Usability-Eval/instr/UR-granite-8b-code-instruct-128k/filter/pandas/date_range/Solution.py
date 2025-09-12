import pandas as pd

# Create a DatetimeIndex with a fixed frequency of 3 days
date_range = pd.date_range(start='2023-01-01', end='2023-02-01', freq='3D')

# Print the DatetimeIndex
print(date_range)
