
import pandas as pd

# Create a sample dataframe
data = {'A': [None, 2, 3, None],
        'B': [5, None, 7, 8],
        'C': [10, None, None, 13]}

df = pd.DataFrame(data)

# Compute the first non-null entry of each column
first_non_null = df.apply(lambda x: x.first_valid_index())

print(first_non_null)
