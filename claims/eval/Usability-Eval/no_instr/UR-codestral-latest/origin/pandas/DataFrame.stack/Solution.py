import pandas as pd

# Assuming 'df' is your DataFrame and 'level_columns' is the list of column names you want to stack
level_columns = ['column1', 'column2']

# Set the specified columns as index
df.set_index(level_columns, inplace=True)

# Now stack the specified levels from columns to index
df = df.stack()
