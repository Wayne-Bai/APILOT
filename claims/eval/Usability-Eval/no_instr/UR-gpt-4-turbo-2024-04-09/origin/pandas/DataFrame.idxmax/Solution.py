import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'A': [1, 2, 5, 4],
    'B': [4, 5, 6, 7],
    'C': [7, 8, 9, 10]
})

# Finding the index of the first occurrence of the maximum value over an axis
# By default, axis=0 (per column), change to axis=1 for per row
index_of_max = df.idxmax()

print(index_of_max)
