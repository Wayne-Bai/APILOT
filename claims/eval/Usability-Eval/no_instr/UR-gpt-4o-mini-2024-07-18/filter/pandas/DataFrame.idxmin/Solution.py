import pandas as pd

# Sample DataFrame
data = {
    'A': [3, 1, 2],
    'B': [4, 5, 1],
    'C': [9, 6, 7]
}

df = pd.DataFrame(data)

# Return index of the first occurrence of minimum over specified axis (0 for columns, 1 for rows)
min_index = df.idxmin(axis=0)  # Change axis=1 for row-wise

print(min_index)
