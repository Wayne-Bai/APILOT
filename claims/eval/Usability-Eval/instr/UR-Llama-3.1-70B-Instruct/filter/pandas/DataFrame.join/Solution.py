# Import the pandas library
import pandas as pd

# Create the first DataFrame
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
}, index=[0, 1, 2, 3])

# Create the second DataFrame
df2 = pd.DataFrame({
    'E': ['E0', 'E1', 'E2', 'E3'],
    'F': ['F0', 'F1', 'F2', 'F3'],
    'G': ['G0', 'G1', 'G2', 'G3'],
    'H': ['H0', 'H1', 'H2', 'H3'],
}, index=[0, 1, 2, 3])

# Join columns of df2 with df1 on the index
df_joined = pd.concat([df1, df2], axis=1)

print("Joined DataFrame:")
print(df_joined)

# Join columns of df2 with df1 on a key column
df1['key'] = [0, 1, 2, 3]
df2['key'] = [0, 1, 2, 3]

df_joined_on_key = pd.merge(df1, df2, on='key')

print("\nJoined DataFrame on key:")
print(df_joined_on_key)

# Efficiently join multiple DataFrame objects by index at once by passing a list
df_list = [df1, df2]
df_joined_multiple = pd.concat(df_list, axis=1)

print("\nJoined multiple DataFrames:")
print(df_joined_multiple)
