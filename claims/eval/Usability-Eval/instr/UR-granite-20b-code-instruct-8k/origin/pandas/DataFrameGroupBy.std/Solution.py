import pandas as pd

# Assuming you have a DataFrame named 'df' with columns 'group' and 'value'
# Compute standard deviation of groups, excluding missing values
df.groupby('group')['value'].transform(lambda x: x.fillna(x.mean()).std())
