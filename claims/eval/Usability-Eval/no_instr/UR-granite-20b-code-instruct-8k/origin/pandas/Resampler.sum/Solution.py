import pandas as pd
# Assuming you have a DataFrame named df with a column named 'group' and a column named 'value'
df.groupby('group')['value'].sum()
