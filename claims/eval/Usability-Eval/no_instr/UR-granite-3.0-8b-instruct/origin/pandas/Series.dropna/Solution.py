import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': [9, 10, 11, None]
})

# Drop rows with missing values
df_dropped = df.dropna()

# Fill missing values with a constant value (e.g., 0)
df_filled = df.fillna(0)

# Fill missing values with the mean of the column
df_filled_mean = df.fillna(df.mean())
