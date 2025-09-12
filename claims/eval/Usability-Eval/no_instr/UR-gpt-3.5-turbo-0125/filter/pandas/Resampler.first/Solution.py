
import pandas as pd

# Create a sample DataFrame
data = {'A': [None, None, 3, 4],
        'B': [None, 6, 7, 8],
        'C': [None, None, None, 12]}

df = pd.DataFrame(data)

# Compute the first non-null entry of each column
first_non_null_values = df.apply(lambda x: x.first_valid_index())

print(first_non_null_values)
