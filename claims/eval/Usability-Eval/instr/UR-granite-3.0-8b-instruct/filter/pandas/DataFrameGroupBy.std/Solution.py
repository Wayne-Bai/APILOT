import pandas as pd

# Assuming df is your DataFrame and 'group' is the column for grouping
df['std_dev'] = df.groupby('group')['value'].transform(lambda x: x.dropna().std())
