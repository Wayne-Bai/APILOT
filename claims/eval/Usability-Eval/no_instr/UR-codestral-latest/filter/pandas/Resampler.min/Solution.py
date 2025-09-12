import pandas as pd

# Assuming we have a DataFrame `df` with columns 'group' and 'value':

min_values = df.groupby('group')['value'].min()

# 'min_values' now contains the minimum value for each unique group in the DataFrame
print(min_values)
