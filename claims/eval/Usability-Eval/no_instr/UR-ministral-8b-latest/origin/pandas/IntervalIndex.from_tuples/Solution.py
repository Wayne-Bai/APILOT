import pandas as pd

# Example data: array of tuples
data = [('2021-01-01', '2021-01-05'), ('2021-01-06', '2021-01-10'), ('2021-01-11', '2021-01-15')]

# Convert data to IntervalIndex
interval_index = pd.date_range(start='2021-01-01', end='2021-01-15', freq="D")[::-2].to_intervals()

# Print the IntervalIndex
print(interval_index)
