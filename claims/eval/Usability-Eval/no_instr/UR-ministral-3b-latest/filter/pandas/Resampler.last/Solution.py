import pandas as pd

# Assuming data is a DataFrame
data = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': ['x', 'y', 'z', None]
})

last_non_null = data.last_valid_index(axis=1)

# Perform elementwise , might not work if data is 2 dimensional
# Extracting the last non-null entry of each column
last_non_null = data.iloc[last_non_null].dropna()

print(last_non_null)
