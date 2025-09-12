import pandas as pd

# Sample DataFrames for demonstration
data1 = {'ID': [1, 2, 3, 4],
         'Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [24, 27, 22, 32]}

data2 = {'ID': [1, 2, 3, 4],
         'Name': ['Alice', 'Bob', 'Charlie', 'Daniel'],
         'Age': [24, 27, 23, 32]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Find differences
comparison = df1.compare(df2)

# Output the differences
print(comparison)
