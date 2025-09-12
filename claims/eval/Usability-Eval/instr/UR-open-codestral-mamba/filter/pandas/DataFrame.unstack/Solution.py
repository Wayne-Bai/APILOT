import pandas as pd

# Assume we have a DataFrame df with a MultiIndex as index
df = pd.DataFrame({
    'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
    'B': ['one', 'one', 'two', 'two', 'one', 'one'],
    'C': ['small', 'large', 'small', 'small', 'large', 'large'],
    'D': [1, 2, 3, 4, 5, 6],
    'E': [10, 20, 30, 40, 50, 60]
})
df = df.set_index(['A', 'B', 'C'])

# Pivot the DataFrame
df_pivot = df.unstack('B')

# If there are more levels in the index, flatten the index
df_pivot.columns = df_pivot.columns.map('_'.join)
