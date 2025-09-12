import pandas as pd

# Assuming you have a DataFrame called 'df' and a column called 'group'
# Compute variance of groups, excluding missing values
variance_by_group = df.groupby('group')['column'].var()

print(variance_by_group)
