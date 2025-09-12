
import pandas as pd

# Prefix labels in Series
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s.index = 'prefix_' + s.index
print(s)

# Prefix labels in DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df.columns = 'prefix_' + df.columns
print(df)
