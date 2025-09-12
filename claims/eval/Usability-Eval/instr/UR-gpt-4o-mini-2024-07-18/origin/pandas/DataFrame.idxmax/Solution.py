import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 3, 5, 2],
    'B': [4, 2, 6, 3]
}
df = pd.DataFrame(data)

# Get the index of the first occurrence of the maximum value along the specified axis
first_max_index = df.idxmax(axis=0)  # Change axis=0 for columns, axis=1 for rows

print(first_max_index)
