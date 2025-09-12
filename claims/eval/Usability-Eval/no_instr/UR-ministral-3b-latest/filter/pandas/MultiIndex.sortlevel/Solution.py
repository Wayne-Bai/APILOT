import pandas as pd

# Sample MultiIndex DataFrame
arrays = [
    ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
    ['one', 'two', 'three', 'one', 'two', 'three']
]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

df = pd.DataFrame({"A": [1, 2, 3, 4, 5, 6]}, index=index)
df.sort_index()