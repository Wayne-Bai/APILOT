import pandas as pd

# Assuming df is your DataFrame and it has a MultiIndex
df = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
}, index=[['A', 'A'], [1, 2], [3, 4], [5, 6]])

# Reset the index to the default one
df = df.reset_index(drop=True)

print(df)
