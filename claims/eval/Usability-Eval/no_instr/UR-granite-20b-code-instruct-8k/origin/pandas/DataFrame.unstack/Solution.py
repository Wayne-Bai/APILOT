import pandas as pd

# Sample data
data = {
    'A': ['foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'bar', 'foo', 'foo', 'foo', 'foo'],
    'B': ['one', 'one', 'one', 'two', 'one', 'one', 'one', 'two', 'two', 'two', 'two', 'one'],
    'C': ['small', 'large', 'large', 'small', 'small', 'small', 'large', 'small', 'small', 'small', 'large', 'small'],
    'D': [1, 2, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7],
    'E': [2, 4, 5, 5, 6, 6, 7, 8, 9, 10, 11, 10]}

df = pd.DataFrame(data)

# Pivot the index labels
pivot_df = df.pivot_table(index=['A', 'B'], columns='C', values='D')

print(pivot_df)
