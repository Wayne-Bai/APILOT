# Import pandas library
import pandas as pd

# Create a sample Series
s = pd.Series([1, 2, 2, 3, 4, 4, 5, 6, 6, 7])

# Remove duplicate values from Series
s = s.drop_duplicates()

# Print the Series
print(s)
