import pandas as pd

# Sample DataFrames to be joined
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value1': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value2': [5, 6, 7, 8]
})

df3 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value3': [9, 10, 11, 12]
})

# Setting the 'key' column as index for efficient joining
df1.set_index('key', inplace=True)
df2.set_index('key', inplace=True)
df3.set_index('key', inplace=True)

# Joining multiple DataFrames on index
result = df1.join([df2, df3])

# Displaying the result
print(result)
