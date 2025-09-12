import pandas as pd
import numpy as np

# Define an array-like of tuples
tuples = [(1, 5), (10, 15), (20, 25), (30, 40)]

# Construct an IntervalIndex from the array-like of tuples
interval_index = pd.IntervalIndex.from_tuples(tuples, closed='left')

# Print the IntervalIndex
print(interval_index)

# Construct an IntervalIndex with a specified closed parameter
interval_index_right = pd.IntervalIndex.from_tuples(tuples, closed='right')
print(interval_index_right)

# Construct an IntervalIndex with intervals of integer type
interval_index_int = pd.IntervalIndex.from_tuples(tuples, dtype=int)
print(interval_index_int)

# Use the intervals as values in a DataFrame
df = pd.DataFrame({'A': [1, 4, 20, 31]})
df['Interval'] = pd.cut(df['A'], bins=interval_index, include_lowest=True)

print(df)
