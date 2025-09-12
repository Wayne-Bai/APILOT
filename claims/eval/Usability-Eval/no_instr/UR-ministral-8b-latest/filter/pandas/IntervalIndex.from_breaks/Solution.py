import pandas as pd

# Example data
data = pd.date_range(start='2023-01-01', periods=10, freq='D').strftime('%Y-%m-%d')

# Define intervals
intervals = pd.to_datetime(['2023-01-04', '2023-01-10', '2023-01-16'])

# Create an IntervalIndex from the intervals
interval_index = pd.IntervalIndex.from_tuples([
    (intervals[0], intervals[0]),
    (intervals[1], intervals[2] - pd.Timedelta(days=1)),
    (intervals[2], intervals[2])
])

# Create a DataFrame with the data and the interval index
df = pd.DataFrame(data, columns=['Date'], index=interval_index)

print(df)
