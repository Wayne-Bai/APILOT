# Import the pandas library
import pandas as pd

# Create DataFrames
df1 = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

df2 = pd.DataFrame({
    'key': ['K0', 'K1', 'K4', 'K5'],
    'C': ['C0', 'C1', 'C4', 'C5'],
    'D': ['D0', 'D1', 'D4', 'D5']
})

df3 = pd.DataFrame({
    'key': ['K1', 'K2', 'K6', 'K7'],
    'E': ['E1', 'E2', 'E6', 'E7'],
    'F': ['F1', 'F2', 'F6', 'F7']
})

# Join df1 and df2 on index
df_joined_1 = df1.join(df2.set_index('key'), lsuffix='_caller', rsuffix='_other')

# Join df1 and df3 on index
df_joined_2 = df1.join(df3.set_index('key'), lsuffix='_caller', rsuffix='_other')

# Join df_joined_1 and df_joined_2 on index
df_joined = df_joined_1.join(df_joined_2.set_index('key'), lsuffix='_caller_1', rsuffix='_caller_2')

# Alternatively, you can join multiple DataFrames at once by passing a list
# First, reset the index of df2 and df3
df2_reset_index = df2.reset_index()
df3_reset_index = df3.reset_index()

# Then, join them to df1
df_joined_multiple = df1.join([df2_reset_index, df3_reset_index], on='key')

print(df_joined)
print(df_joined_multiple)
