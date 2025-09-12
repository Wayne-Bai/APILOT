
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Assign desired index to a specific axis (column B in this case)
new_index = ['X', 'Y', 'Z', 'W', 'V']
df = df.set_index('B')
df.index = new_index

print(df)
