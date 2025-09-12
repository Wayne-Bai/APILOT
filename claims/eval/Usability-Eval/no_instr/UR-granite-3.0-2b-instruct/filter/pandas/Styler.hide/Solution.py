import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Hide the entire index
df_hidden_index = df.reset_index(drop=True)

# Hide specific rows
df_hidden_rows = df.iloc[:2]

# Hide specific columns
df_hidden_columns = df.loc[:, ['A', 'B']]

# Print the dataframes
print("DataFrame with hidden index:")
print(df_hidden_index)
print("\nDataFrame with hidden rows:")
print(df_hidden_rows)
print("\nDataFrame with hidden columns:")
print(df_hidden_columns)
