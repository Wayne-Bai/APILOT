
import pandas as pd

data = [(0, 5), (10, 15), (20, 25), (30, 35)]
interval_index = pd.IntervalIndex.from_tuples(data)

print(interval_index)
