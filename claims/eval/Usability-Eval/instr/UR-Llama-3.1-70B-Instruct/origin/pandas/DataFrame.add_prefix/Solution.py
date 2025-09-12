# Import the pandas library
import pandas as pd

# Create a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Prefix labels with string 'prefix_'
df.columns = ['prefix_' + col for col in df.columns]

print("DataFrame with prefixed column labels:")
print(df)

# Create a Series
s = pd.Series([10, 20, 30], index=['X', 'Y', 'Z'])

# Prefix index labels with string'series_prefix_'
s.index = ['series_prefix_' + idx for idx in s.index]

print("\nSeries with prefixed index labels:")
print(s)
