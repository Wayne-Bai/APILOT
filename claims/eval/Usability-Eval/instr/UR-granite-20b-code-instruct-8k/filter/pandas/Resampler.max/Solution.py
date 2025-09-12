import pandas as pd

# Assuming you have a DataFrame named df

# Compute max value of group
max_value_per_group = df.groupby('column_to_group').max()

