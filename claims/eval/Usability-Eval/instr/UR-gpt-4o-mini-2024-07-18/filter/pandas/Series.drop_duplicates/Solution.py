import pandas as pd

# Sample Series
data = pd.Series([1, 2, 2, 3, 4, 4, 5])

# Remove duplicates
unique_series = data.drop_duplicates()

# Display the result
print(unique_series)
