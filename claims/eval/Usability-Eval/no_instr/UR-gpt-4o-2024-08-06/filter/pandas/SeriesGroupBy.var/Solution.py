import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 10, None, 30, 40]
}

df = pd.DataFrame(data)

# Compute variance of groups, excluding missing values
variance_by_group = df.groupby('Category', as_index=False).agg({'Values': 'var'})

print(variance_by_group)
