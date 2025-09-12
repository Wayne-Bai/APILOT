import pandas as pd

# Sample DataFrame
data = {
    'Column_1': [1, 2, 3, 4],
    'Column_2': ['A', 'B', 'C', 'D'],
    'Column_3': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

# Hide the entire index
df_index_hidden = df.copy()
df_index_hidden.index = None

# Hide specific columns
df_columns_hidden = df.copy()
df_columns_hidden['Column_2'] = None

# Hide specific rows
df_rows_hidden = df.copy()
df_rows_hidden.iloc[1:-1] = None

print(df_index_hidden)
print(df_columns_hidden)
print(df_rows_hidden)
