
import pandas as pd

# Create a Series with duplicate values
data = pd.Series([1, 2, 2, 3, 3, 4, 5])

# Remove duplicate values from the Series
result = data.drop_duplicates()

print(result)
