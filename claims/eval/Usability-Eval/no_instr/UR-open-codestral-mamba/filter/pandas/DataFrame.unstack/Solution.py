import pandas as pd

# Assuming we have a DataFrame df with a hierarchical index
df = pd.DataFrame({
    'A': ['a', 'a', 'b', 'b', 'b'],
    'B': ['one', 'two', 'one', 'two', 'two'],
    'C': ['small', 'large', 'small', 'small', 'large'],
    'D': [1, 2, 3, 4, 5],
    'E': [5, 4, 3, 2, 1]
}).set_index(['A', 'B', 'C'])

# Using 'unstack' to pivot the level of the index labels
pivot_df = df.unstack('B')

# Output the pivot DataFrame
pivot_df

