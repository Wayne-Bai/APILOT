
import pandas as pd

# Creating a sample DataFrame
data = {'A': [4, 3, 1, 2],
        'B': [5, 2, 7, NaN],
        'C': [1, NaN, 3, 4]}
df = pd.DataFrame(data)

# Finding index of first occurrence of minimum value over columns (axis=1)
min_index = df.idxmin(axis=1)

print(min_index)
