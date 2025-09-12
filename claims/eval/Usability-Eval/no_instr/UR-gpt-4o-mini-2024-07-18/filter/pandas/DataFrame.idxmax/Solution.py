import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 3, 5, 7],
    'B': [2, 3, 1, 9],
    'C': [5, 6, 2, 8]
}

df = pd.DataFrame(data)

# Get the index of the first occurrence of the maximum value over axis 0 (columns)
first_max_index = df.idxmax(axis=0)

print(first_max_index)
