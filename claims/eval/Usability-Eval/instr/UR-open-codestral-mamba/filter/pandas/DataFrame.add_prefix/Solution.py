import pandas as pd

# Suppose we have the following series
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# To prefix the labels, we can append a string to the index
s.index = 'my_prefix' + s.index

print(s)

# Similarly, for dataframes, we can append a string to the column labels
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
df.columns = 'my_prefix' + df.columns

print(df)
