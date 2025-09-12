import pandas as pd
import numpy as np

# Example DataFrame
data = {
    'A': [None, 2, None, 4],
    'B': [1, None, None, None],
    'C': [None, None, 3, 4],
    'D': [None, None, None, None]
}

df = pd.DataFrame(data)

# Method to find the last non-null entry in each column
last_non_nulls = df.apply(lambda col: col[col.last_valid_index()] if col.last_valid_index() is not None else None)

print(last_non_nulls)
