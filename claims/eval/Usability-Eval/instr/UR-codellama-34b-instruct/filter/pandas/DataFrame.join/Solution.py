
import pandas as pd

# create two sample DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})

# join the two DataFrames on column A and C
result = df1.join(df2, on='A', how='inner')

print(result)
