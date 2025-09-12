import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4, 5],
    'B': ['a', 'b', 'c', 'd', None],
    'C': ['x', None, 'z', 'y', 'w'],
    'D': [True, False, None, True, False]
})

# Inferring dtypes for object (string) columns
df['B'] = df['B'].astype(pd.StringDtype())
df['C'] = df['C'].astype(pd.StringDtype())
df
