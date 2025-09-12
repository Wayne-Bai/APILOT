import pandas as pd

# Create a date range with a fixed frequency
date_range = pd.date_range(start='1/1/2022', end='12/31/2022', freq='D')

# Create a DataFrame with the DatetimeIndex
df = pd.DataFrame(index=date_range)
