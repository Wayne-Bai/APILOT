import pandas as pd

# Creating a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['key1', 'key2', 'key3'])

# Hiding the entire index
print("Hiding entire index:")
df_hidden_index = df.reset_index(drop=True)
print(df_hidden_index)

# Hiding specific keys in the index
keys_to_hide = ['key1', 'key3']
df_hidden_specific_keys = df[~df.index.isin(keys_to_hide)]
print("\nHiding specific keys in the index:")
print(df_hidden_specific_keys)
