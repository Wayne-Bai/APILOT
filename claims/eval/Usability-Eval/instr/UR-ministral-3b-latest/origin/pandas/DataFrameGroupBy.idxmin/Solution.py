import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, None],
    'B': [2, 3, None, 4, 5],
    'C': [2, 3, 4, None, 5]
})

# Requested axis (for demonstration, let's select 'axis=0' - rows)
axis = 0

# Compute the index of the first occurrence of the minimum value over the requested axis
min_index = pd.DataFrame.index(df.idxmin(axis=axis)).min()

print(min_index)
