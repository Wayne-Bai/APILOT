
import pandas as pd

# create a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# assign custom index to rows
custom_index = ['X', 'Y', 'Z']
df.index = custom_index

print(df)
