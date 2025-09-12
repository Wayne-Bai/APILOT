import pandas as pd

# Assuming you have two DataFrames: df1 and df2
# df1
#    A   B
# 0  1   x
# 1  2   y

# df2
#    A   B
# 0  1   z
# 1  3   y

# Find rows which are different between the two DataFrames
diff = pd.concat([df1, df2]).drop_duplicates(keep=False)
print(diff)
