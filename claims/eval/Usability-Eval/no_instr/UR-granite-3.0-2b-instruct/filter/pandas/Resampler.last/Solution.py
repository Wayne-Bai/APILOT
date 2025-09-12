import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4, None],
    'B': [None, 6, 7, 8, None],
    'C': [9, 10, 11, None, 13]
})

# Compute the last non-null entry of each column
last_non_null = df.last(ignore_index=True)

print(last_non_null)
