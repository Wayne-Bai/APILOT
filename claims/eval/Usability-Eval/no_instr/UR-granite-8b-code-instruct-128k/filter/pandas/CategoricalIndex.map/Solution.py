
import pandas as pd

# Example usage:
# Create a series
s = pd.Series([1, 2, 3, 4, 5])

# Define a mapping dictionary
mapping = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

# Apply the mapping to the series
mapped_series = s.map(mapping)

print(mapped_series)
