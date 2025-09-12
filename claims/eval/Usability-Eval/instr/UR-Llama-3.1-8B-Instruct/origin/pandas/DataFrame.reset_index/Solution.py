# Import necessary libraries
import pandas as pd

# Create a sample DataFrame with MultiIndex
data = {
    'A': ['one', 'one', 'one', 'two', 'two', 'two'],
    'B': ['x', 'y', 'z', 'x', 'y', 'z'],
    'C': [1, 2, 3, 4, 5, 6],
    'D': [2, 4, 6, 8, 10, 12]
}
df = pd.DataFrame(data)
df.set_index(['A', 'B'], inplace=True)

# Reset the index of the DataFrame, and use the default one instead
df_reset = df.reset_index()

# Print the original DataFrame with MultiIndex
print("Original DataFrame:")
print(df.head())

# Print the new DataFrame with default index
print("Default Index DataFrame:")
print(df_reset.head())
