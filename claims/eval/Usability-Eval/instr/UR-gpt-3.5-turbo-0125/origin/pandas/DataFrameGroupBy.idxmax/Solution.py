
import pandas as pd

# Create a sample dataframe
data = {'A': [10, 20, 30, 40],
        'B': [25, 15, 35, 45],
        'C': [20, 35, 15, 25]}
df = pd.DataFrame(data)

# Find the index of the first occurrence of maximum value along a specific axis (axis=0 for columns, axis=1 for rows)
max_index_column = df.idxmax().values[0]
max_index_row = df.idxmax(axis=1).values[0]

print("Index of the first occurrence of maximum value along columns: ", max_index_column)
print("Index of the first occurrence of maximum value along rows: ", max_index_row)
