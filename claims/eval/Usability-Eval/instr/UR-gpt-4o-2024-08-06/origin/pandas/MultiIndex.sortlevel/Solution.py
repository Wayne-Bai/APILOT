import pandas as pd

# Creating a sample DataFrame with a MultiIndex
index = pd.MultiIndex.from_tuples(
    [('A', 1), ('A', 2), ('B', 1), ('B', 2), ('C', 1)],
    names=['First', 'Second']
)
data = {'Values': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data, index=index)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Sort the MultiIndex DataFrame at a specific level
# Let's say we want to sort by the 'Second' level
sorted_df = df.sort_index(level='Second')

# Display the sorted DataFrame
print("\nSorted DataFrame by 'Second' level:")
print(sorted_df)
