import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, None],
    'B': [4, None, 6],
    'C': [None, None, 9]
})

# Remove missing values
df_cleaned = df[df.notnull().all(axis=1)]

print(df_cleaned)
