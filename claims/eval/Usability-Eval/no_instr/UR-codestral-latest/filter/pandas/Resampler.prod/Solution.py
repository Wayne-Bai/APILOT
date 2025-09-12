import pandas as pd

# Assuming you have a DataFrame df with columns 'Group' and 'Value'
df['Product'] = df.groupby('Group')['Value'].transform(lambda x: x.prod())
