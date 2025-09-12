import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, None, 4],
    'B': [None, None, 'foo', 'bar'],
    'C': [None, 5, 6, None],
}

df = pd.DataFrame(data)

# Compute the last non-null entry of each column
last_non_null = df.where(pd.notnull(df)).bfill().iloc[-1]

print(last_non_null)
