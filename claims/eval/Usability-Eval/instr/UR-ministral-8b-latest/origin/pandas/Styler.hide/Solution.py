import pandas as pd

# Sample DataFrame for demonstration
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Option to hide the entire index
df_no_index = df.rename_axis('')
print("DataFrame without index and column names:")
print(df_no_index)

# Option to hide specific columns
df_hidden_columns = df[['Name', 'City']]
print("\nDataFrame with specific columns (Age column hidden):")
print(df_hidden_columns)

# Option to hide specific rows
filtered_df = df[df['Age'] > 30]
print("\nDataFrame with specific rows (Age > 30):")
print(filtered_df)

# Option to hide specific column names
df_no_column_headers = df.rename(columns={'Name': 'N', 'Age': 'A', 'City': 'C'})
print("\nDataFrame without specific column names:")
print(df_no_column_headers)
