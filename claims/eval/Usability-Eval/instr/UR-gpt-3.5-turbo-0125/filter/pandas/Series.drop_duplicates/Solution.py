
import pandas as pd

# Create a sample Series
data = pd.Series([1, 2, 2, 3, 4, 4, 5])

# Remove duplicate values
result = data.drop_duplicates()

print(result)
