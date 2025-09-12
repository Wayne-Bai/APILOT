import pandas as pd

# Example Series
s = pd.Series(['a', 'b', 'c'], index=['x', 'y', 'z'])
print("Original Series:")
print(s)

# Prefixing series
s_prefix = s.add_prefix('new__')
print("Series with Prefixed Labels:")
print(s_prefix)

# Example DataFrame
df = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
}, index=['x', 'y'])
print("Original DataFrame:")
print(df)

# Prefixing DataFrame column labels
df_prefix = df.rename(columns=lambda x: f'new_{x}')
print("DataFrame with Prefixed Column Labels:")
print(df_prefix)
