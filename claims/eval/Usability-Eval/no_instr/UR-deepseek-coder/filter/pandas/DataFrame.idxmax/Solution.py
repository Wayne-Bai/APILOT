import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 20, 10],
    'C': [5, 4, 3, 2, 1]
}

df = pd.DataFrame(data)

# Return the index of the first occurrence of the maximum over the requested axis
max_index_axis_0 = df.idxmax(axis=0)
max_index_axis_1 = df.idxmax(axis=1)

print("Index of first occurrence of maximum over axis 0:")
print(max_index_axis_0)

print("\nIndex of first occurrence of maximum over axis 1:")
print(max_index_axis_1)
