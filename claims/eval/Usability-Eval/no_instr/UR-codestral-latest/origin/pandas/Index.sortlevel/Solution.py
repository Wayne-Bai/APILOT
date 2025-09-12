import pandas as pd

# Assuming 'df' is your DataFrame and 'idx' is the desired index

# For a Single Index
df.sort_index(inplace=True)

# For a MultiIndex
df.sort_index(level=[0, 1], inplace=True)
# Here, level=[0,1] means sort by the first level then by the second level. Adjust the levels as needed per your data.
