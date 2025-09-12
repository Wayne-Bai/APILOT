import pandas as pd

# Assuming df is your DataFrame and 'group' and 'value' are the columns
df['max_value'] = df.groupby('group')['value'].transform('max')
