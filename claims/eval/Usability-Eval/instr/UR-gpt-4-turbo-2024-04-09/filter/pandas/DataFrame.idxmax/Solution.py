import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 2],
    'B': [4, 5, 6, 5]
})

# Find the index of the first occurrence of the maximum value over the default axis (axis=0 for columns)
max_index = df.idxmax()

print(max_index)
