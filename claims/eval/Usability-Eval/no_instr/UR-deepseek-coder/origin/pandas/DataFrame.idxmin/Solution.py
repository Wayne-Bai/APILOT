import pandas as pd

# Example DataFrame
data = {
    'A': [3, 2, 2, 4, 1],
    'B': [1, 3, 2, 4, 5],
    'C': [4, 3, 2, 1, 5]
}

df = pd.DataFrame(data)

# Find the index of the first occurrence of the minimum value over the requested axis
min_index = df.idxmin(axis=0)

print(min_index)
