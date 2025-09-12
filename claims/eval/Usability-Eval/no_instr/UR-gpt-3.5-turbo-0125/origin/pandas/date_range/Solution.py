
import pandas as pd

# Creating a DatetimeIndex with fixed frequency
date_index = pd.date_range('2022-01-01', periods=10, freq='D')

print(date_index)
