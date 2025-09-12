import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})

# Calculate the maximum value over the rows
max_row = df.max(axis=1)

# Get the index of the first occurrence of the maximum value over each row
max_row_idx = max_row.idxmax()

print(max_row_idx)
