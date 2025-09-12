
import pandas as pd

# Create a sample DataFrame with MultiIndex
arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['number', 'color'])
df = pd.DataFrame({'data': [1, 2, 3, 4]}, index=index)

# Sort MultiIndex at the requested level ('color' in this case)
df_sorted = df.sort_index(level='color')

print(df_sorted)
