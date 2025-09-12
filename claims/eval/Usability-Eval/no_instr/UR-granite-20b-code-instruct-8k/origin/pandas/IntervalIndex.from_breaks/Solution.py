import pandas as pd

splits = [1, 3, 5, 7, 9]
interval_index = pd.IntervalIndex.from_breaks(splits)
print(interval_index)
