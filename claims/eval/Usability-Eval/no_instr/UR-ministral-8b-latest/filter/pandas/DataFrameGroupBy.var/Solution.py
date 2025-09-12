import pandas as pd

# Sample data
data = {
    'group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'value': [5, None, 7, 2, 5, None, 3, 2, 2]
}

df = pd.DataFrame(data)

# Compute variance of groups, excluding missing values
df['value'] = df['value'].dropna()  # Drop rows with missing values in 'value' column
grouped_df = df.groupby('group')['value']

variances = grouped_df.var()
print(variances)
