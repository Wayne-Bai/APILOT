import pandas as pd

# Create a fixed frequency DatetimeIndex starting from January 1, 2023, with daily frequency
datetime_index = pd.date_range(start='2023-01-01', periods=10, freq='D')

print(datetime_index)
