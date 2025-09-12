import pandas as pd

# Creating the first DataFrame
df1 = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

print("DataFrame 1:")
print(df1)

# Creating the second DataFrame
df2 = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

print("\nDataFrame 2:")
print(df2)

# Joining DataFrames on a key column
df_joined = pd.merge(df1, df2, on='key')
print("\nJoined DataFrame on 'key' column:")
print(df_joined)

# Joining DataFrames on index
df1.set_index('key', inplace=True)
df2.set_index('key', inplace=True)
df_joined_index = df1.join(df2, how='inner', lsuffix='_caller', rsuffix='_other')
print("\nJoined DataFrame on index:")
print(df_joined_index)

# Joining multiple DataFrames at once
df3 = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'E': ['E0', 'E1', 'E2', 'E3'],
    'F': ['F0', 'F1', 'F2', 'F3']
})
df_joined_multiple = df1.join([df2, df3], how='inner', lsuffix='_caller', rsuffix='_other')
print("\nJoined multiple DataFrames at once:")
print(df_joined_multiple)
