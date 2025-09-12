
import pandas as pd

# create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# find index of first occurrence of maximum value over requested axis (column-wise)
print(df.idxmax())
