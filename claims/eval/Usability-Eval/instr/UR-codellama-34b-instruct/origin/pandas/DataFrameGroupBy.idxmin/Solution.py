
import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# calculate the index of the minimum value in each row
idx_min = df.idxmin(axis=1)
print(idx_min)
