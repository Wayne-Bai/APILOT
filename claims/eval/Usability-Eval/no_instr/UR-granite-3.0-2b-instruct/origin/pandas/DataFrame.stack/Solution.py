import pandas as pd

# Assuming df is your DataFrame and 'level_columns' is a list of columns to stack
df.stack(level=level_columns, dropna=False, inplace=True)
