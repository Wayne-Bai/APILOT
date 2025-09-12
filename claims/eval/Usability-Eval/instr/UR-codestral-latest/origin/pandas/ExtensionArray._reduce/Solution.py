import pandas as pd

# Assuming df is your DataFrame
# Let's say you want to sum all values in the first column ('Column1')

result = df['Column1'].sum()

# If you wish to apply the sum operation on multiple columns, use the below code
result = df[['Column1', 'Column2']].sum().sum()  # First .sum() to get column-wise sum and second .sum() to get total sum

# If you wish to get row-wise sum, use the below code
result = df.sum(axis=1)
