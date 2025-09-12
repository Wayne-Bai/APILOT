
import pandas as pd

# Create a DatetimeIndex with a frequency of every minute
index = pd.date_range(start='2023-01-01', end='2023-01-31', freq='T')

print(index)
