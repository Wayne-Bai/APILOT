
import pandas as pd

# create a sample DataFrame
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# create another sample DataFrame with some differences
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

# use the merge() method to compare the two DataFrames and show the differences
result = df1.merge(df2, how='outer', indicator=True)

print(result)
