
import pandas as pd

# create a sample series with duplicate values
s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

# remove duplicates and keep only the first occurrence
s = s.drop_duplicates()

print(s)
