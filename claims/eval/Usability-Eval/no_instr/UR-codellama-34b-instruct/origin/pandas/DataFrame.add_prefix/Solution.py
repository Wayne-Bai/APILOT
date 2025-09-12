
import pandas as pd

# Create a sample Series and DataFrame
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
df = pd.DataFrame({'A': [4, 5, 6], 'B': [7, 8, 9]}, index=['d', 'e', 'f'])

# Prefix labels for Series and DataFrame with string 'prefix_'
s = s.rename(lambda x: f"prefix_{x}")
df = df.rename(columns=lambda x: f"prefix_{x}", axis='index')

print(s)
print(df)
