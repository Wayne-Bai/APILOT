
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, None, 4],
        'B': [None, 5, 6, None],
        'C': [7, None, None, None]}

df = pd.DataFrame(data)

# Compute the last non-null entry of each column
last_non_null = df.apply(lambda x: x.last_valid_index())

print(last_non_null)
