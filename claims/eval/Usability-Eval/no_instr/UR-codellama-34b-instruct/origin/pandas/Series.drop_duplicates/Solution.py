
import pandas as pd

# create a sample Series with some duplicate values
s = pd.Series(['a', 'b', 'c', 'd', 'e', 'a'])
print(s)

# use drop_duplicates method to remove duplicates
s = s.drop_duplicates()
print(s)
