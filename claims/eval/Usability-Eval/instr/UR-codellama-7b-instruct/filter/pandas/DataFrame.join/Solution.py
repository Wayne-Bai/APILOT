
import pandas as pd

# create sample DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]}, index=['a', 'b', 'd'])
df3 = pd.DataFrame({'E': [13, 14, 15], 'F': [16, 17, 18]}, index=['c', 'd', 'e'])

# join DataFrames by index
df_merged = pd.merge(df1, df2, how='outer')
print(df_merged)

# join DataFrames by key column
df_merged = pd.merge(df1, df3, on='A', how='outer')
print(df_merged)

# join multiple DataFrame objects at once by index
dfs = [df1, df2, df3]
df_merged = pd.concat([pd.DataFrame({col: df[col] for col in df.columns}) for df in dfs], how='outer')
print(df_merged)
