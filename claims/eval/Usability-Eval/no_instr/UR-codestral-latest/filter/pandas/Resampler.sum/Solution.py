import pandas as pd

# Assuming df is the DataFrame and 'group' is the column on which you want to group
df['sum'] = df.groupby('group')['values'].transform('sum')
