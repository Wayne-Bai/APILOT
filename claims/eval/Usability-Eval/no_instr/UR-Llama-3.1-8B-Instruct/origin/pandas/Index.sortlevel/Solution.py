import pandas as pd

# Sample data for demonstration
index = pd.MultiIndex.from_tuples([
    ('alpha', 'one'), ('alpha', 'two'),
    ('beta', 'one'), ('beta', 'two'),
    ('alpha', 'one'), ('alpha', 'three')
], names=['first','second'])

# Create a DataFrame with the MultiIndex
df = pd.DataFrame({
    'C': 1,
    'D': 4},
    index=index)

# This is for internal compatibility with the Index API
# Sort the Index. This is for compat with MultiIndex
print("Original DataFrame:")
print(df)

sorted_index = df.index.get_duplicates().sort_values()

print("\nSorted DataFrame:")
df = df.reindex(sorted_index, level=0)

print(df)
