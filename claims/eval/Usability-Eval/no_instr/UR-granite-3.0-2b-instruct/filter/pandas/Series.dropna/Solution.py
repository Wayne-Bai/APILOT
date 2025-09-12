import pandas as pd

# Assuming df is your DataFrame and it has missing values
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 6, 7, 8],
    'C': [9, 10, 11, None]
})

# Remove missing values
df = df.dropna()
