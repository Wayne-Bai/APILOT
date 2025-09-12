import pandas as pd

# Series with row labels
ser = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
ser.index = ser.index.map(lambda x: 'prefix_' + x)
ser

# DataFrame with column labels
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
df.columns = df.columns.map(lambda x: 'prefix_' + x)
df
