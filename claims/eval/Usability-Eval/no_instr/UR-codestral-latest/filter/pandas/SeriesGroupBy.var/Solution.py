import pandas as pd

# Assuming you have a DataFrame `df` and a column `group` to group by
# Replace `df`, `group` and `value` with your actual DataFrame and column names
variances = df.groupby('group')['value'].var(skipna=True)
