import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [None, 2, 3, None],
    'B': [None, None, 5, 6],
    'C': [1, 2, None, 4]
})

# Compute the first non-null entry of each column
first_non_null = df.apply(lambda x: x.dropna().first() if x.dropna().notna().any() else None, axis=0)

print(first_non_null)
