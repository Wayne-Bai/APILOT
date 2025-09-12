import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Hide specific rows from display (e.g., row at index 1)
hidden_rows_df = df.drop(index=[1])

# Hide specific columns from display (e.g., column 'B')
hidden_columns_df = df.drop(columns=['B'])

# Hide entire index from display
df_no_index = df.to_string(index=False)

# Hide entire column headers from display
df_no_columns = df.to_string(header=False)

# Display results
print("DataFrame with specific rows hidden:\n", hidden_rows_df, "\n")
print("DataFrame with specific columns hidden:\n", hidden_columns_df, "\n")
print("DataFrame with entire index hidden:\n", df_no_index, "\n")
print("DataFrame with entire column headers hidden:\n", df_no_columns)
