
import pandas as pd

# create a sample series
data = pd.Series([1, 2, 3, 4, 5])

# remove duplicates using the 'unique' method
duplicates_removed = data.unique()

print(duplicates_removed)
