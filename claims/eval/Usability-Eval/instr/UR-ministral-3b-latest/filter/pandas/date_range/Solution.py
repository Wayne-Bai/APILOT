import pandas as pd

# Create a simple DatetimeIndex with an incremental time frequency
date_range = pd.date_range(start='2023-01-01', end='2023-01-10', freq='1D')
print(date_range)
