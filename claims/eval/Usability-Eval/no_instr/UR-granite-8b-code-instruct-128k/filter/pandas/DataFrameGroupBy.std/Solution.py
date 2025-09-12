import pandas as pd

# Assuming you have a DataFrame called 'df' with columns 'group' and 'value'
# and a list of groups called 'groups'

# Compute standard deviation of groups, excluding missing values
std_dev = df.groupby('group')['value'].std()
