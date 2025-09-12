import pandas as pd

# Assume we have two dataframes: df1 and df2
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

# Compare the two dataframes and show the differences
print(pd.compare_frame(df1, df2))
