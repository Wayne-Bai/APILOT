import pandas as pd

# Assuming you have a pandas Series called 'series' with duplicate values
series = pd.Series([1, 2, 2, 3, 4, 4, 5])

# Use the 'drop_duplicates' method to remove duplicate values from the Series
series_without_duplicates = series.drop_duplicates()

# Print the resulting Series without duplicate values
print(series_without_duplicates)
