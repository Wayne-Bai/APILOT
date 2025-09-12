import pandas as pd

# Assuming df is the pandas DataFrame
df['column_name'] = df['column_name'].apply(lambda x: x + '_suffix')
