import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [4, 2, 8, 1],
    'B': [10, 20, 30, 40],
    'C': [100, 50, 30, 20]
})

# Finding the index of the first occurrence of the minimum over an axis.
# Here we choose axis 0 for minimum value in each column
min_index = df.idxmin(axis=0)

print(min_index)
