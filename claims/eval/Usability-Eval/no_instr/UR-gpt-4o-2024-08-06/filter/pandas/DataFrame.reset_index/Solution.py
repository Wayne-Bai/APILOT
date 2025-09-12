import pandas as pd

# Sample data to create a DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}

# Creating a DataFrame with a default index
df = pd.DataFrame(data)

# Set a specific column as the index
df.set_index('A', inplace=True)

# Resetting the index of the DataFrame to the default integer index
df_reset = df.reset_index()

# To reset a specific level in a MultiIndex DataFrame, assume df_multi is defined
# Example for MultiIndex DataFrame
arrays = [
    ['bar', 'bar', 'baz', 'baz'],
    ['one', 'two', 'one', 'two']
]
index = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))
df_multi = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}, index=index)

# Reset only the 'second' level of the MultiIndex
df_multi_reset = df_multi.reset_index(level='second')

# Print results
print("Reset single-level index DataFrame:\n", df_reset)
print("\nReset specific level in MultiIndex DataFrame:\n", df_multi_reset)
