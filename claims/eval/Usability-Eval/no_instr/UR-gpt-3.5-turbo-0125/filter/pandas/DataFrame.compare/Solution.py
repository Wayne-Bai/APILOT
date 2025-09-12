
import pandas as pd

# Create two sample DataFrames
data1 = {'A': [1, 2, 3, 4],
         'B': [10, 20, 30, 40]}
df1 = pd.DataFrame(data1)

data2 = {'A': [1, 2, 5, 4],
         'B': [10, 20, 50, 40]}
df2 = pd.DataFrame(data2)

# Find differences between two DataFrames
differences = df1.compare(df2)
print(differences)
