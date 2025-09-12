import pandas as pd

# Assuming you have an array-like of tuples
data = [('a', 1), ('b', 2), ('c', 3)]

# Creating a Series from the data
series = pd.Series(data)

# Creating an IntervalIndex from the Series
interval_index = pd.IntervalIndex.from_tuples(series.values)

# Creating a DataFrame using the Series and IntervalIndex
df = pd.DataFrame(series, index=interval_index)
print(df)
