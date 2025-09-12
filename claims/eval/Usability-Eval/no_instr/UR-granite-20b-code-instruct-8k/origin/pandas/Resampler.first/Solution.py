import pandas as pd

# Assuming df is the DataFrame with your data
df = pd.DataFrame({'A': [None, 2, 3],
                   'B': [1, 2, None],
                   'C': [None, None, 3]})

# Compute the first non-null entry of each column
first_non_null = df.first_valid_index()

print(first_non_null)
