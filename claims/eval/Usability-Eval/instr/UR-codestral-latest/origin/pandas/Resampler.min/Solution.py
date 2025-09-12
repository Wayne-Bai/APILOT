import pandas as pd

# Let's assume you have a pandas DataFrame 'df' with columns 'group' and 'value'
# Replace 'df', 'group' and 'value' with your actual DataFrame and column names

min_val_per_group = df.groupby('group')['value'].min()
