import pandas as pd

# Assuming df1 and df2 are your DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [1, 2, 4], 'B': [4, 5, 7]})

# Find the differences between the two DataFrames
diff = df1[df1 != df2]

print(diff)
