import pandas as pd

# Example DataFrame with a hierarchical index
data = {
    'values': [10, 20, 30, 40],
    'category': ['A', 'A', 'B', 'B']
}
index = pd.MultiIndex.from_tuples(
    [(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y')],
    names=['first', 'second']
)
df = pd.DataFrame(data, index=index)

# Pivoting the index
pivoted_df = df.pivot_table(values='values', index='category', columns=df.index.get_level_values(0), aggfunc='sum')

# Display the result
print(pivoted_df)
