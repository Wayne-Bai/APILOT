import pandas as pd

# Let's assume we have a DataFrame df, and we're grouping by a column 'group'
# We're computing the standard deviation of another column 'value'

# Exclude missing values
std_dev = df.dropna(subset=['value'])

# Compute standard deviation of 'value' column, grouped by 'group' column
std_dev_grouped = std_dev.groupby('group')['value'].std()
