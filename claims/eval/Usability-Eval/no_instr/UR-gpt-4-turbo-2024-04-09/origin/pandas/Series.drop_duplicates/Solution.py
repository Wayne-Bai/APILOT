import pandas as pd

# Sample series data
data = pd.Series([1, 2, 2, 3, 4, 4, 5])

# Remove duplicate values
unique_data = data.drop_duplicates()

print(unique_data)
