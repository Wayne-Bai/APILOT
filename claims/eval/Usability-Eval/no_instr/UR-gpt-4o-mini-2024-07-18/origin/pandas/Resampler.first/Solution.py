import pandas as pd

# Sample DataFrame
data = {
    'A': [None, 2, 3, None],
    'B': [1, None, None, 4],
    'C': [None, None, 5, 6]
}

df = pd.DataFrame(data)

# Compute the first non-null entry of each column
first_non_null = df.apply(lambda x: x.dropna().iloc[0] if not x.dropna().empty else None)

print(first_non_null)
