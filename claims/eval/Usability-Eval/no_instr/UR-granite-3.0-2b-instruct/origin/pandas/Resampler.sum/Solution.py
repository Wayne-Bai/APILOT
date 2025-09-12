import pandas as pd

# Assuming df is your DataFrame and 'group' and 'value' are columns
grouped = df.groupby('group')
result = grouped['value'].sum()
