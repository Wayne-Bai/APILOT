import pandas as pd

# Sample DataFrame with MultiIndex
arrays = [
    ['a', 'a', 'b', 'b'],
    [1, 2, 1, 2]
]
index = pd.MultiIndex.from_arrays(arrays, names=('letters', 'numbers'))
df = pd.DataFrame({'value': [10, 20, 30, 40]}, index=index)

print("Original DataFrame with MultiIndex:")
print(df)

# Resetting the index to default and removing the 'numbers' level of the MultiIndex
df_reset = df.reset_index(level='numbers')

print("\nDataFrame after resetting 'numbers' level of MultiIndex:")
print(df_reset)

# Fully resetting the index to default and removing all levels
df_reset_full = df.reset_index()

print("\nDataFrame after fully resetting the index:")
print(df_reset_full)
