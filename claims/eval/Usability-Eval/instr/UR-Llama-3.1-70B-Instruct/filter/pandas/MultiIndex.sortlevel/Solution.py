import pandas as pd

# Creating a MultiIndex DataFrame
data = {
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
}

df = pd.DataFrame(data)

# Setting the index to create a MultiIndex
df = df.set_index(['A', 'B'])

# Original DataFrame
print("Original DataFrame:")
print(df)

# Sorting the MultiIndex at level 0
df_sorted_lvl0 = df.sort_index(level=0)

# DataFrame sorted at level 0
print("\nDataFrame sorted at level 0 (A):")
print(df_sorted_lvl0)

# Sorting the MultiIndex at level 1
df_sorted_lvl1 = df.sort_index(level=1)

# DataFrame sorted at level 1
print("\nDataFrame sorted at level 1 (B):")
print(df_sorted_lvl1)
