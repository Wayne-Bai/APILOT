import pandas as pd

# Example DataFrame
data = {
    ('A', 'cat1'): [1, 2, 3],
    ('A', 'cat2'): [4, 5, 6],
    ('B', 'cat1'): [7, 8, 9],
    ('B', 'cat2'): [10, 11, 12],
}

df = pd.DataFrame(data, index=['row1', 'row2', 'row3'])
df.columns = pd.MultiIndex.from_tuples(df.columns)

# Stack the level 'B' from columns to index
stacked_df = df.stack(level=0)

print("Original DataFrame:\n", df)
print("\nStacked DataFrame:\n", stacked_df)
