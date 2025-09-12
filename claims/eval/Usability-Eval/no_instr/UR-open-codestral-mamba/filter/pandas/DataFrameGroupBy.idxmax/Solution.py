import pandas as pd

# Assuming the dataframe df is already declared and populated with data
# If you don't have a dataframe, you can create a simple one like so:
# df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [3, 1, 2, 4]})

# Assume 'axis' is 1 (meaning you want to find maximum along columns)
axis = 1

# Find the indices of maximum values along the given axis
max_indices = df.idxmax(axis=axis)

# Find the index of first occurrence of maximum
first_max_index = max_indices.argmin()
first_max_index
