import pandas as pd
from pandas.api.types import IntervalIndex

# Sample array-like of tuples
data = [(10, 20), (30, 40), (50, 60)]

# Creating for the IntervalIndex
index = IntervalIndex.from_tuples(data)
print(index)
