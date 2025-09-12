
import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['apple', 'banana', 'cherry']})
df2 = pd.DataFrame({'C': [4, 5, 6], 'D': ['dog', 'cat', 'fish']})

# Join on index
result = df1.merge(df2, how='outer')
print(result)

# Join on key column
result = df1.merge(df2, how='outer', on='A')
print(result)

# Join multiple DataFrames at once by index
dfs = [df1, df2]
result = pd.concat(dfs, axis=1)
print(result)
