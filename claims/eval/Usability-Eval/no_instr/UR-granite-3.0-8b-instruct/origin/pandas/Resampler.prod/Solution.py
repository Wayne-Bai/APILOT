import pandas as pd

# Assuming df is your DataFrame and 'group' and 'value' are your columns
df['product'] = df.groupby('group')['value'].transform(lambda x: x.prod())
