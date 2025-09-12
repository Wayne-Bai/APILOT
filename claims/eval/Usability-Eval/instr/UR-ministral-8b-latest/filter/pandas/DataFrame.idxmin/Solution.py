import pandas as pd

# Sample DataFrame
data = {'A': [2, 3, 1, 4],
        'B': [1, 3, 2, 4]}
df = pd.DataFrame(data)

# Get the index of the first occurrence of the minimum value in the specified axis (axis=0 for rows, axis=1 for columns)
min_index = df.idxmin(axis=0)

print(min_index)
