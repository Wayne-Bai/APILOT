import pandas as pd

# Assume you have a DataFrame `df`
# If you're working with a column
first_max_index_column = df['column_name'].idxmax()

# If you're working with a row
first_max_index_row = df.loc[df.max(axis=1).idxmax()]

# If you're working with the entire DataFrame
first_max_index_dataframe = df.stack().idxmax()
