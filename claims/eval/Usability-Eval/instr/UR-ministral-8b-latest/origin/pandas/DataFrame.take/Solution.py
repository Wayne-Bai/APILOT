import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12],
    'D': [13, 14, 15, 16]
})

# If we want to return elements at specific indices along the column axis
# Indexing; to get the third and fifth rows (indices 2 and 4), element-wise for column df['A']
columns_index = [2, 4]
result_columns = df.ix[:, df.columns.tolist()]

# Indexing; to get the third and fifth rows (indices 2 and 4), element-wise for column df['A']
rows_index = [2, 4]
result_rows = df[df.columns]
result_rows.loc[rows_index, df.index.tolist()]

print("Result Columns:\n", result_columns)
print("\nResult Rows:\n", result_rows)
