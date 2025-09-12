import pandas as pd

# Sample DataFrames for demonstration
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [10, 20, 30]
})

df2 = pd.DataFrame({
    'key': ['A', 'B', 'D'],
    'value2': [15, 25, 35]
})

# Set the 'key' column as the index for both DataFrames
df1.set_index('key', inplace=True)
df2.set_index('key', inplace=True)

# Join the DataFrames on their index
result = df1.join(df2, how='outer')

print(result)
