# Import the pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
}
index = pd.MultiIndex.from_tuples([('foo', 'one'), ('foo', 'two'), ('foo', 'one'), ('foo', 'two')],
                                  names=['first','second'])
df = pd.DataFrame(data, index=index)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Reset the index of the DataFrame
df_reset = df.reset_index()

# Print the DataFrame with the reset index
print("\nDataFrame with the reset index:")
print(df_reset)

# Reset the index of the DataFrame and drop the first level
df_reset_single_level = df.reset_index(level=0)

# Print the DataFrame with a single level of the index
print("\nDataFrame with a single level of the index:")
print(df_reset_single_level)

# Reset the index of the DataFrame and drop the first two levels
df_reset_two_levels = df.reset_index(level=[0, 1])

# Print the DataFrame with two levels of the index removed
print("\nDataFrame with two levels of the index removed:")
print(df_reset_two_levels)
