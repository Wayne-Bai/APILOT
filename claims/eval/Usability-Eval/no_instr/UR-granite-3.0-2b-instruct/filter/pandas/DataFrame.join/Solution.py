import pandas as pd

# Assuming df1 and df2 are your DataFrames and 'key' is the common column
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'key': ['K0', 'K1', 'K2', 'K3']
})

df2 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
    'key': ['K0', 'K1', 'K2', 'K3']
})

# Join DataFrame on 'key' column
df3 = pd.merge(df1, df2, on='key')

print(df3)
