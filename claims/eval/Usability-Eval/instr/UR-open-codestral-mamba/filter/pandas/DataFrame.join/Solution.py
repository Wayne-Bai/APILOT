import pandas as pd

# Create a sample DataFrame
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'key1': ['K0', 'K1', 'K1', 'K2']
})

df2 = pd.DataFrame({
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
    'key1': ['K0', 'K1', 'K1', 'K2']
})

df3 = pd.DataFrame({
    'E': ['E0', 'E1', 'E2', 'E3'],
    'F': ['F0', 'F1', 'F2', 'F3'],
    'key1': ['K0', 'K1', 'K1', 'K3']
})

# Combine all DataFrame objects into a single DataFrame
dfs = [df1, df2, df3]
result = pd.concat(dfs, keys=['df1', 'df2', 'df3'])

result
