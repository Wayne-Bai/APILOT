import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 6, 7, 8],
    'C': [10, 11, 12, None]
})

# Compute the last non-null entry of each column
df_last_non_null = df.ffill().loc[:, df.columns != 'index']
