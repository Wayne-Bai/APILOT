
import pandas as pd

# Create a sample series
s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Use the unique() method to remove duplicates and return a new series
unique_s = s.unique()

print(unique_s)
