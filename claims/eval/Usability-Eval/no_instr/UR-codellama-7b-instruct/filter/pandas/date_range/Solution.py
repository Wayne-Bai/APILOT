
import pandas as pd

# Create a DatetimeIndex with a fixed frequency of 'D' (daily) starting from 2010-01-01
index = pd.date_range('2010-01-01', periods=365, freq='D')

print(index)
