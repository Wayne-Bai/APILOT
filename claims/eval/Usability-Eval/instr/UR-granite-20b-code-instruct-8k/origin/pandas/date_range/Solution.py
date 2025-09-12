import pandas as pd

# Create a DatetimeIndex with a fixed frequency
index = pd.date_range('2022-01-01', periods=10, freq='D')

# Print the DatetimeIndex
print(index)
