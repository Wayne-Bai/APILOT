import pandas as pd

# Assuming df is your DataFrame and it has missing values
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': [9, 10, 11, None]
})

# To remove rows with missing values
df_dropped = df.dropna()

# To remove columns with missing values
df_dropped = df.dropna(axis=1)
