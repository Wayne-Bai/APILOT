import pandas as pd

# Assuming df is our DataFrame df['A'] is our column and we want to set 'A' as the index for axis 0
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df = df.set_index('A')

# Alternatively, to set 'A' as the index for axis 1
df = df.T # Transpose the DataFrame
df = df.set_index('A')
df = df.T # Transpose the DataFrame back
