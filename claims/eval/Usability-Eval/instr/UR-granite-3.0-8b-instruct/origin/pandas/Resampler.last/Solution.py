import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 6, 7, 8],
    'C': [9, 10, 11, None]
})

# Compute the last non-null entry of each column
last_non_null = df.apply(lambda x: x.dropna().iloc[-1], axis=0)

print(last_non_null)
