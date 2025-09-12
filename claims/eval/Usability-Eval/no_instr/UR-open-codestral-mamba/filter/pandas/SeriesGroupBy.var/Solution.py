import pandas as pd

# Let's assume this is your DataFrame
df = pd.DataFrame({
    'Group': ['A', 'A', 'B', 'B', 'A', 'A'],
    'Value': [1, 2, 3, None, 5, 6]
})

# Compute the variance excluding missing values
variance_per_group = df.groupby('Group')['Value'].var(skipna=True)

print(variance_per_group)
