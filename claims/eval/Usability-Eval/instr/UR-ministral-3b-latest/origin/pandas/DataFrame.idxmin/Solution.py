import pandas as pd

# Assume df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 4, 5, 6]
})
print(df)

# Find the index of first occurrence of minimum over each column
axis_min_index = df.idxmin(axis=1)
print(axis_min_index)
