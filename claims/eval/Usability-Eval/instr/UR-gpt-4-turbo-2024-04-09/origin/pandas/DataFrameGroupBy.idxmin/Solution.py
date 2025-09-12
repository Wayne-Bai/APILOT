import pandas as pd

# example DataFrame
data = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 1, 6],
    'C': [7, 8, 2]
})

# Get the index of the minimum value in a specific column
index_min_A = data['A'].idxmin()

# Get the index of the minimum value across an entire row axis
index_min_row = data.idxmin(axis=1)

# Output the results
print("Index of minimum value in column A:", index_min_A)
print("Indexes of minimum values across rows:", index_min_row)
