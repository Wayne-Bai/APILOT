import pandas as pd

# Create a sample MultiIndex DataFrame
index = pd.MultiIndex.from_tuples([
    ('A', 1), ('A', 2), ('B', 1), ('B', 2)
], names=['Letter', 'Number'])

data = {
    'Value1': [10, 20, 30, 40],
    'Value2': [100, 200, 300, 400]
}

df = pd.DataFrame(data, index=index)

# Pivot the 'Number' level of the index to become columns
pivoted_df = df.unstack(level='Number')

print(pivoted_df)
