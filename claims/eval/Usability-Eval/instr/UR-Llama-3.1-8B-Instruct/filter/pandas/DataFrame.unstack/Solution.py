import pandas as pd

# Create a multi-index DataFrame
index = pd.MultiIndex.from_tuples(
    [
        ('cat', 'apple', 1),
        ('cat', 'banana', 2),
        ('dog', 'apple', 1),
        ('dog', 'berry', 2),
        ('cat', 'apple', 1),
        ('cat', 'banana', 2),
    ],
    names=['animal', 'fruit', 'id']
)
data = {
    'value1': [10, 10, 20, 20, 10, 10],
    'value2': [100, 100, 200, 200, 100, 100],
}

df = pd.DataFrame(data, index=index)

# Pivot the inner-most level of the index
pivoted_df = df.reset_index().pivot_table(
    index=['animal', 'fruit'],
    columns='id',
    values='value1'
)

print(pivoted_df)
