
import pandas as pd

# Sample data
data = {'A': [1, None, None], 'B': [2, 3, None], 'C': [4, None, 6]}
df = pd.DataFrame(data)

# Compute first non-null entry of each column
first_non_null_entries = df.notna().cumsum()

print(first_non_null_entries)
