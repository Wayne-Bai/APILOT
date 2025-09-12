import pandas as pd

# Assuming df is your DataFrame and 'group' is the column used for grouping
variances = df.groupby('group')['column'].var()  # replace 'column' with your column name
