import pandas as pd

# Sample DataFrame creation
data = {
    ('A', 'one'): [1, 2, 3],
    ('A', 'two'): [4, 5, 6],
    ('B', 'one'): [7, 8, 9],
    ('B', 'two'): [10, 11, 12]
}

index = pd.MultiIndex.from_tuples([(0, 'foo'), (1, 'bar'), (2, 'baz')], names=['number', 'type'])
df = pd.DataFrame(data, index=index)

# Pivoting a level of the index labels
pivoted_df = df.stack(level=0).unstack(level=0)

print(pivoted_df)
