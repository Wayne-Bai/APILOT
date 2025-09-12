import pandas as pd

# Sample DataFrame
data = {
    'A': [1, None, 3, 4],
    'B': [None, 2, None, 4],
    'C': [1, 2, 3, None]
}

df = pd.DataFrame(data)

# Compute the last non-null entry in each column
last_non_null = df.apply(lambda col: col.dropna().iloc[-1])

print(last_non_null)
