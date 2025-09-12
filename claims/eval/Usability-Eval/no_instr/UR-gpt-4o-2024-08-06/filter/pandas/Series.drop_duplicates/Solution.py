import pandas as pd

# Sample data
data = [1, 2, 3, 4, 3, 2, 5]

# Create a pandas Series
series = pd.Series(data)

# Return Series with duplicate values removed
unique_series = series.drop_duplicates()

print(unique_series)
