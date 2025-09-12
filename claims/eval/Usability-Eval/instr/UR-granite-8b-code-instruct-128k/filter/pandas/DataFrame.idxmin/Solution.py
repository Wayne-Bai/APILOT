import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
    'A': [1, 2, 3, 2, 1],
    'B': [4, 5, 6, 5, 4],
    'C': [7, 8, 9, 8, 7]
})

# Return the index of the first occurrence of the minimum value over the rows
print(df.idxmin())
