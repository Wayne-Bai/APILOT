import pandas as pd

# Assuming df is your DataFrame and it has a MultiIndex with levels 'A' and 'B'
df = pd.DataFrame({
    'value': [1, 2, 3, 4, 5, 6],
    'index': pd.MultiIndex.from_tuples([
        ('X', 'a'), ('X', 'b'), ('Y', 'c'), ('Y', 'd'), ('Y', 'e'), ('Y', 'f')
    ])
})

# Sort the DataFrame at level 'A' while preserving the original ordering of the associated factor at that level
df = df.sort_index(level='A', inplace=False)

print(df)
