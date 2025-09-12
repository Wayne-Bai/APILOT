import pandas as pd

# Sample Series with duplicate values
data = pd.Series([1, 2, 2, 3, 4, 4, 5])

# Return Series with duplicate values removed
unique_series = data.drop_duplicates()

print(unique_series)
