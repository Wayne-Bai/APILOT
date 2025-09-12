import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'A': [1, 2, np.nan, 4],
    'B': [4, 0, 3, 1],
    'C': [np.nan, np.nan, 2, 5],
}

df = pd.DataFrame(data)

# Find the index of the first occurrence of the minimum value over each column
index_of_min = df.idxmin(axis=0)

print(index_of_min)
