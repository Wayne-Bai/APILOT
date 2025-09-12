import pandas as pd

# Assuming df1 and df2 are your DataFrames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'key': ['K0', 'K1', 'K2', 'K3']},
                   index=['I0', 'I1', 'I2', 'I3'])

df2 = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3'],
                    'key': ['K0', 'K1', 'K2', 'K3']},
                   index=['I0', 'I1', 'I2', 'I3'])

# Joining DataFrames on 'key' column
df3 = pd.merge(df1, df2, on='key')

# Alternatively, you can join on index
df4 = pd.merge(df1, df2, left_index=True, right_index=True)
