import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 3, 2],
    'B': [4, 5, 1],
    'C': [7, 8, 6]
}
df = pd.DataFrame(data)

# Get the index of the first occurrence of the maximum values along the specified axis
first_max_index = df.idxmax(axis=0)  # Change axis=0 for columns, axis=1 for rows
print(first_max_index)
