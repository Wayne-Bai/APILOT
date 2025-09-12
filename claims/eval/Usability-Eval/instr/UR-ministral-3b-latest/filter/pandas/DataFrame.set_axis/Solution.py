import pandas as pd

# Example DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Assign desired axis index
new_index = ['one', 'two', 'three']
df.index = new_index

print(df)
