
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4],
        'B': [7, 8, 9, 2],
        'C': [2, 7, 5, 3]}
df = pd.DataFrame(data)

# Find the index of the first occurrence of maximum value along columns (axis=1)
index_max = df.idxmax(axis=1).tolist()
print(index_max)
