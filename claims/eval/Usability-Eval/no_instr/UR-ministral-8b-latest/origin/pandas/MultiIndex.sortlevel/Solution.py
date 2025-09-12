import pandas as pd

# Example DataFrame with MultiIndex
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
}
index = pd.MultiIndex.from_tuples([('x', 1), ('x', 2), ('y', 1), ('y', 2), ('x', 3)],
                                  names=['level1', 'level2'])
df = pd.DataFrame(data, index=index)

# Sorting MultiIndex at level 'level2'
df_sorted = df.sort_index(level='level2')

print(df_sorted)
