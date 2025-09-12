import pandas as pd

# Create a DatetimeIndex with a frequency of 3 days
dti = pd.date_range(start='2022-01-01', periods=10, freq='3D')

# Print the DatetimeIndex
print(dti)
