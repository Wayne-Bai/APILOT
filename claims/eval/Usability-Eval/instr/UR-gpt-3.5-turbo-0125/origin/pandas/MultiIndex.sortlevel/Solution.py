
import pandas as pd

# Create a sample DataFrame with MultiIndex
arrays = [['A', 'A', 'B', 'B'], ['foo', 'bar', 'foo', 'bar']]
index = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))
df = pd.DataFrame({'data': [1, 2, 3, 4]}, index=index)

# Sort the MultiIndex at the 'first' level
df = df.sort_index(level='first')

# Display the sorted DataFrame
print(df)
