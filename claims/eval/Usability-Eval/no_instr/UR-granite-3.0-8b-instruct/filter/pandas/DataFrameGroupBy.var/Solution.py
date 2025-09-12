import pandas as pd

# Assuming df is your DataFrame and 'group' is the column for grouping
grouped = df.groupby('group')

# Compute variance of groups, excluding missing values
variance = grouped.apply(lambda x: x[x.notna()].var())
