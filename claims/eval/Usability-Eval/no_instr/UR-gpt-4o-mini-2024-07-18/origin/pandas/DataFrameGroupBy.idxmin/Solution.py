import pandas as pd

# Sample DataFrame
data = {
    'A': [3, 1, 2, None],
    'B': [4, 5, 6, None],
    'C': [None, 1, 0, 2]
}
df = pd.DataFrame(data)

# Return index of first occurrence of minimum over requested axis (0 for columns, 1 for rows)
index_min = df.idxmin(axis=0)  # Change axis=1 for row-wise minimum
print(index_min)
