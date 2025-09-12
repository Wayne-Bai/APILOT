import pandas as pd
# Create a sample DataFrame
df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar'],
    'B': ['one', 'two', 'two', 'one'],
    'C': np.random.randn(4),
    'D': np.random.randn(4)
}, index=[['a', 'a'], ['b', 'b'], ['c', 'c'], ['d', 'd']])
# Pivot the index labels
df_pivot = df.pivot_table(index=df.index.droplevel(0), columns='B')
print(df_pivot)
