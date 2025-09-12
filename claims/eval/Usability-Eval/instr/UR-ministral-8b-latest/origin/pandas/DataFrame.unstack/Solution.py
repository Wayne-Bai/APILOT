import pandas as pd

# Sample DataFrame with hierarchical index
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
}
index = pd.MultiIndex.from_tuples([('x', 'a', 'b'), ('x', 'b', 'c'), ('y', 'a', 'd'), ('y', 'a', 'e')])
df = pd.DataFrame(data, index=index)

# Pivot the outer level of the index labels to the dataframe columns
pivoted_df = df.unstack(level=0)

print(pivoted_df)
