import pandas as pd

# Assuming df is your DataFrame and 'group' is the column for grouping
df['group'] = df['group'].fillna('Unknown')  # Replace missing values in 'group' with 'Unknown'
grouped = df.groupby('group')

variances = grouped['value'].var(skipna=True)  # Compute variance of 'value' for each group, excluding missing values

print(variances)
