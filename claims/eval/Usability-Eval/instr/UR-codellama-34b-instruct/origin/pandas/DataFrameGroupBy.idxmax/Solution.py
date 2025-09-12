import pandas as pd

# Assuming 'df' is your DataFrame, you can find the index of the first occurrence of the maximum value over a specified axis (e.g., 0 for rows or 1 for columns) using the following code:
max_index = df.index[df.idxmax(axis=1)]

# If you want to get the row and column index of the first occurrence of the maximum value, you can use the following code:
row_index, col_index = np.where(df == max_index)
