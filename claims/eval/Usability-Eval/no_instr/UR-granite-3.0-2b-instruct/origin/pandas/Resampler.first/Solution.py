import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [None, 2, 3, None, 5],
    'B': [None, None, 4, 5, 6],
    'C': [1, 2, None, 4, 5]
})

# Compute the first non-null entry of each column
first_non_null = df.apply(lambda x: x.first_valid_index() if not pd.isna(x.first_valid_index()) else None, axis=1)

print(first_non_null)
