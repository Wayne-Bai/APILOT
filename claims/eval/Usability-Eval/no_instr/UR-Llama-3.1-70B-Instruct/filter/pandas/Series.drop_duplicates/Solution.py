# Import the pandas library
import pandas as pd

# Create a Series
series = pd.Series([1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8])

# Display the original series
print("Original Series:")
print(series)

# Use the drop_duplicates method to remove duplicates
series_without_duplicates = series.drop_duplicates()

# Display the series with duplicates removed
print("\nSeries with duplicates removed:")
print(series_without_duplicates)
