
# Importing pandas library
import pandas as pd

# Create a MultiIndex
arrays = [['A', 'A', 'A', 'B', 'B', 'B'],
          ['1', '2', '3', '1', '2', '3']]
tuples = list(zip(*arrays))
multi_index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

# Create a sample Series with MultiIndex
s = pd.Series(range(6), index=multi_index)

# Sort the MultiIndex
sorted_index = s.index.sort_values()

# Display the sorted MultiIndex
print(sorted_index)
