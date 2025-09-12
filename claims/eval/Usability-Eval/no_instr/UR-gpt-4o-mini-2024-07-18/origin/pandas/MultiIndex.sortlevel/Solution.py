import pandas as pd

# Sample data for demonstration
index = pd.MultiIndex.from_tuples(
    [('A', 1), ('A', 2), ('B', 1), ('B', 3), ('B', 2)],
    names=['first', 'second']
)
data = [5, 3, 6, 1, 2]
df = pd.DataFrame(data, index=index, columns=['values'])

# Sorting the MultiIndex DataFrame by level 'first'
sorted_df = df.sort_index(level='first', sort_remaining=False)

print(sorted_df)
