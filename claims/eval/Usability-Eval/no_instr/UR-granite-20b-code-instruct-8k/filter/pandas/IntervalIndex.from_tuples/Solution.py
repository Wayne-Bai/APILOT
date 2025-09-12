import pandas as pd

tuples = [(1, 3), (4, 6), (7, 9)]
index = pd.IntervalIndex.from_tuples(tuples)
print(index)
