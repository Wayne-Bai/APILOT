import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 3, 5],
    'B': [5, 6, 7],
    'C': [9, 11, 10]
})

# Return the index of the first occurrence of the maximum value over the requested axis
# axis=0 for row-wise, axis=1 for column-wise
index_of_max = df.idxmax(axis=0)

print(index_of_max)
