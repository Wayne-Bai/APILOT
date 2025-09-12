import pandas as pd

# Assuming df is the DataFrame you want to modify
df['column_name'] = df['column_name'].apply(lambda x: x + '_suffix')
