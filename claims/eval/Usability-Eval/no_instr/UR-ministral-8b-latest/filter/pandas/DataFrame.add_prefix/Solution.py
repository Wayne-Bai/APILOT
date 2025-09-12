import pandas as pd

# Example Series
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s1_prefix = s1.add_prefix('prefix_')
print("Prefixed Series:\n", s1_prefix)

# Example DataFrame
df = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [15, 25, 35]
})
df_prefix = df.add_prefix('prefix_')
print("\nPrefixed DataFrame:\n", df_prefix)
