import pandas as pd

# Assuming df is your DataFrame and 'column1' and 'column2' are the columns you want to add suffixes to
df['column1_suffix'] = df['column1'].apply(lambda x: x + '_suffix')
df['column2_suffix'] = df['column2'].apply(lambda x: x + '_suffix')
