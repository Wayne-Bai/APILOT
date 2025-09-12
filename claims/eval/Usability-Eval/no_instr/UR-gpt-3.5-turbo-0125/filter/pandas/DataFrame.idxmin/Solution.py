
import pandas as pd

# Create a sample DataFrame
data = {'A': [10, 20, 30],
        'B': [5, 10, 5],
        'C': [15, 15, 15]}
df = pd.DataFrame(data)

# Find the index of the first occurrence of the minimum value along the column axis
min_index = df.idxmin(axis=0)

print(min_index)
