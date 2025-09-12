import pandas as pd

# Example data to create a MultiIndex DataFrame
arrays = [
    ['A', 'A', 'B', 'B'],
    ['one', 'two', 'one', 'two']
]
index = pd.MultiIndex.from_arrays(arrays, names=('letters', 'numbers'))
data = pd.DataFrame({'value': [1, 2, 3, 4]}, index=index)

# Sorting the MultiIndex DataFrame
sorted_data = data.sort_index()

print(sorted_data)
