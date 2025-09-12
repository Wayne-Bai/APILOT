
import pandas as pd

data = [(0, 5), (7, 12), (15, 20)]
interval_index = pd.IntervalIndex.from_tuples(data)

print(interval_index)
