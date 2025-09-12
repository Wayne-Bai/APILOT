import pandas as pd

# Sample DataFrame with object columns
data = {
    'int_column': ['1', '2', '3', '4'],
    'float_column': ['1.1', '2.2', '3.3', '4.4'],
    'string_column': ['a', 'b', 'c', 'd'],
    'bool_column': ['True', 'False', 'True', 'False']
}

df = pd.DataFrame(data)

# Use pandas' built-in functionality to infer better dtypes
df = df.convert_dtypes()

# Print the results to verify type inference
print(df.dtypes)
print(df)
