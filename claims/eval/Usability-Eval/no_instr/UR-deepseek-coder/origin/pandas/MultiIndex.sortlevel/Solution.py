import pandas as pd

# Sample DataFrame with MultiIndex
index = pd.MultiIndex.from_tuples([
    ('A', 'X', 1),
    ('A', 'Y', 2),
    ('B', 'X', 3),
    ('B', 'Y', 4)
], names=['First', 'Second', 'Third'])

data = {'Values': [10, 20, 30, 40]}
df = pd.DataFrame(data, index=index)

# Sort MultiIndex at the 'Second' level
df_sorted = df.sort_index(level='Second', sort_remaining=False)

print(df_sorted)
