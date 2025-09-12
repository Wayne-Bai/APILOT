import pandas as pd

# Assuming 's' is your Series
s = pd.Series([1, 2, 2, 3, 4, 4, 5, 6, 6])

# Removing duplicates
s_without_duplicates = s.drop_duplicates()

print(s_without_duplicates)
