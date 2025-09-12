import pandas as pd

# Assuming df is your DataFrame and 'group' is the column that groups the data
df = pd.DataFrame({
    'group': ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'value': [1, 2, 3, 4, 5, 6, 7, 8]
})

# Compute variance of groups, excluding missing values
variance_by_group = df.groupby('group')['value'].apply(lambda x: x.var() if x.isnull().sum() == 0 else None).reset_index()

print(variance_by_group)
