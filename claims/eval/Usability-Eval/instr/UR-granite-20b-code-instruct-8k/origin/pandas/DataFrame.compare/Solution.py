import pandas as pd

# Load the first DataFrame
df1 = pd.read_csv('file1.csv')

# Load the second DataFrame
df2 = pd.read_csv('file2.csv')

# Compare the two DataFrames and show the differences
print(df1.compare(df2))
