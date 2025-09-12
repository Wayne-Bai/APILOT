import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'City': ['New York', 'Chicago', 'Los Angeles']
}

df = pd.DataFrame(data)

# Hide the entire index
df_no_index = df.to_string(index=False)

# Hide specific columns
df_no_specific_columns = df.drop(columns=['Age'])

# Hide specific rows (e.g., first row)
df_no_specific_rows = df.drop(index=[0])

# Display results
print("DataFrame without index:")
print(df_no_index)

print("\nDataFrame without specific columns (Age):")
print(df_no_specific_columns)

print("\nDataFrame without specific rows (first row):")
print(df_no_specific_rows)
