import pandas as pd

# Create a MultiIndex DataFrame
index = pd.MultiIndex.from_arrays([['cat1', 'cat1', 'cat2', 'cat2'], ['1st', '2nd', '1st', '2nd']])
df = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                   'B': ['B0', 'B1', 'B2', 'B3']},
                   index=index)

# Sort the DataFrame at the first level
df_sorted = df.sort_index(level=0)

# Print the sorted DataFrame
print(df_sorted)
