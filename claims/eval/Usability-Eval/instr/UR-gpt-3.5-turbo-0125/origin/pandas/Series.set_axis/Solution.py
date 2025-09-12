
import pandas as pd

data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# Assign desired index to axis (rows in this case)
new_index = ['w', 'x', 'y', 'z']
df = df.set_index(pd.Index(new_index))

print(df)
