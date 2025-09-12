import pandas as pd

# Sample data
data = {'A': [1, 2, np.nan, 4],
        'B': [np.nan, 5, 6, 7],
        'C': [3, np.nan, 9, 10]}
df = pd.DataFrame(data)

# Find the first occurrence of minimum over a requested axis
first_index = df.apply(lambda x: x.first_valid_index())
