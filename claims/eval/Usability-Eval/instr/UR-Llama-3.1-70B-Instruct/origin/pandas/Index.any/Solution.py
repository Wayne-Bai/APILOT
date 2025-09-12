# Import pandas library
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [True, False, True],
    'C': [5, 6, 7]
})

# Apply the any method to return whether any element in a column or the entire DataFrame is Truthy
print(df['A'].to_numpy().any())  # Returns: True
print(df['B'].to_numpy().any())  # Returns: True
print(df.to_numpy().any())       # Returns: True

# Test with empty DataFrame or Series
df_empty = pd.DataFrame({
    'A': pd.Series([], dtype=int),
    'B': pd.Series([], dtype=bool),
    'C': pd.Series([], dtype=int)
})
print(df_empty['A'].to_numpy().any())  # Returns: False
print(df_empty['B'].to_numpy().any())  # Returns: False
print(df_empty.to_numpy().any())       # Returns: False
