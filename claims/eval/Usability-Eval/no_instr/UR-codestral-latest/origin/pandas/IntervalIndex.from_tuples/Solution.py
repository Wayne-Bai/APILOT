import pandas as pd

# Suppose intervals are given as [(start1, end1), (start2, end2), ...]
intervals = [(0, 2), (5, 10), (12, 15)]

# Construct an IntervalIndex
index = pd.IntervalIndex.from_tuples(intervals)
