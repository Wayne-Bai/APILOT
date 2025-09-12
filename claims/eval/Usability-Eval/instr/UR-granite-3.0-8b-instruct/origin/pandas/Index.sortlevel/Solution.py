import pandas as pd

# Assuming df is your DataFrame and 'index_column' is the column you want to sort by
df = df.set_index('index_column', drop=False, inplace=False)
df = df.sort_index()
