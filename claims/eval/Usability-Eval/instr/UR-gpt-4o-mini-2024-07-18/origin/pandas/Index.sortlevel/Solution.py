import pandas as pd

# Example MultiIndex DataFrame
arrays = [
    ['A', 'A', 'B', 'B'],
    [1, 2, 1, 2]
]
index = pd.MultiIndex.from_arrays(arrays, names=('letters', 'numbers'))
df = pd.DataFrame({'values': [10, 20, 30, 40]}, index=index)

# Sorting the MultiIndex
df_sorted = df.sort_index()

print(df_sorted)
