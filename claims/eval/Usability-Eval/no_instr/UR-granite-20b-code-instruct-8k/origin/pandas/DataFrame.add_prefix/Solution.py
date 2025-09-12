import pandas as pd

# Series
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)

# DataFrame
df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8]}, index=['a', 'b', 'c', 'd'])
print(df)
