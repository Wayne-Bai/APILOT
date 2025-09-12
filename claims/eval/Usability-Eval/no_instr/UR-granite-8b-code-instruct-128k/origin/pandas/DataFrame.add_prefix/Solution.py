import pandas as pd

# Create a Series
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# Prefix the labels with 'x_'
s = s.rename(lambda x: 'x_' + x)

print(s)
