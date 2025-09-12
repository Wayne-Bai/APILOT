import pandas as pd

# Sample MultiIndex DataFrame
arrays = [
    ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c'],
    [2, 1, 3, 3, 2, 1, 1, 3]
]

index = pd.MultiIndex.from_arrays(arrays, names=('letters', 'numbers'))
df = pd.DataFrame({'values': range(len(index))}, index=index)

# Sort by the second level 'numbers', respecting the original 'letters' ordering
sorted_df = df.sort_index(level='numbers', sort_remaining=False)

print(sorted_df)
