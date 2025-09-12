import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, None, 4]
})

# Compute the first non-null entry of each column
first_non_null = df.loc[:, df.columns[df.apply(lambda x: x.first_valid_index())].notna()]

print(first_non_null)
