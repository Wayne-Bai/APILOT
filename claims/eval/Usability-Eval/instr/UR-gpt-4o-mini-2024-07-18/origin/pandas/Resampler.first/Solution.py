import pandas as pd

# Sample DataFrame
data = {
    'A': [None, 2, 3],
    'B': [None, None, 6],
    'C': [7, None, 9]
}

df = pd.DataFrame(data)

# Compute the first non-null entry of each column
first_non_nulls = df.apply(lambda x: x[x.first_valid_index()] if x.first_valid_index() is not None else None)

print(first_non_nulls)
