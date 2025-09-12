import pandas as pd

# Assume df is the DataFrame and 'column' is the column to calculate standard error for
# Group by 'column' and calculate standard error of the mean
df.groupby('column').sem()
