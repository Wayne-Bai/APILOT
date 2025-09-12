import pandas as pd

# Assuming df is your DataFrame and 'group' is the column for grouping
# and 'value' is the column containing the values

# Drop missing values
df = df.dropna(subset=['group', 'value'])

# Group by 'group' and compute the mean of 'value'
grouped = df.groupby('group')['value'].mean()

# Compute standard error of the mean
std_err = grouped.std() / grouped.count() ** 0.5

print(std_err)
