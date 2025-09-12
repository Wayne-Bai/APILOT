import pandas as pd

# Assuming df is your DataFrame and 'column1' and 'column2' are the hierarchical index labels
df = pd.DataFrame({'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
                   'B': ['one', 'two', 'three', 'one', 'two', 'three'],
                   'C': [1, 2, 3, 4, 5, 6],
                   'D': [7, 8, 9, 10, 11, 12]})

# Set 'column1' and 'column2' as the hierarchical index
df.set_index(['column1', 'column2'], inplace=True)

# Pivot the index label 'column2'
pivoted_df = df.pivot(index='column1', columns='column2', values='C')

# Reset the index to get the pivoted level as a column label
pivoted_df = pivoted_df.reset_index()

print(pivoted_df)
