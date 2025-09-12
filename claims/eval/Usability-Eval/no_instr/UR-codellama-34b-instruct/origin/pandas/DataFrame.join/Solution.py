
import pandas as pd

# create two sample DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})

# join df2 to df1 on the index
joined_df = pd.concat([df1, df2], axis=1)
print(joined_df)
