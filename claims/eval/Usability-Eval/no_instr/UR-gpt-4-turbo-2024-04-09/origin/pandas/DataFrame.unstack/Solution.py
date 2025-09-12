import pandas as pd

# Sample DataFrame setup with a multi-index
data = {
    'Value': [1, 2, 3, 4],
    'Category': ['A', 'B', 'A', 'B']
}
idx = [('X', 'a'), ('X', 'b'), ('Y', 'a'), ('Y', 'b')]
index = pd.MultiIndex.from_tuples(idx, names=['Letter', 'Subletter'])
df = pd.DataFrame(data, index=index)

# Pivot a level of the multi-index to columns
pivoted_df = df.unstack(level='Subletter')

print(pivoted_df)
