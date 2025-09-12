import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 5, 1, 4]
}

df = pd.DataFrame(data)

# Return the index of the first occurrence of the maximum over the requested axis
max_index = df.idxmax(axis=0)

print(max_index)
