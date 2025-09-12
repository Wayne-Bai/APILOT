import pandas as pd

# Assuming you have a DataFrame named df with the required data

# Compute the max value of group
max_value = df.groupby('column_name').max()

# If you want to reset the index
max_value_reset = max_value.reset_index()
