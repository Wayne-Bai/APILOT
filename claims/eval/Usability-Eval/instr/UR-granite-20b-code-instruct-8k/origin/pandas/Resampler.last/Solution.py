import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4, 5],
    'B': [None, 2, 3, 4, None],
    'C': [1, 2, 3, 4, 5],
})

# Compute the last non-null entry of each column
last_non_null = df.last_valid_index()

print(last_non_null)
