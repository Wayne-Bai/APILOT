import pandas as pd

data = [(1, 3), (5, 7), (9, 11)]
index = pd.IntervalIndex.from_tuples(data)
print(index)
