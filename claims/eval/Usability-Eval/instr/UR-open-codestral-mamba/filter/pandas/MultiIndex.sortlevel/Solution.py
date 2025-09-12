import pandas as pd

# Assuming we have a multi-index DataFrame df
data = {
    'A': ['foo', 'foo', 'foo', 'foo', 'bar', 'bar', 'bar', 'bar'],
    'B': ['one', 'one', 'two', 'two', 'one', 'one', 'two', 'two'],
    'C': ['x', 'y', 'x', 'y', 'x', 'y', 'x', 'y'],
    'D': [1, 2, 3, 4, 1, 2, 3, 4]
}
df = pd.DataFrame(data)

# Let's assume we want to sort on level=0, which is 'A'
df_sorted = df.sort_values(by=['A', 'B', 'C', 'D'], ascending=[True, True, True, True])

print(df_sorted)
