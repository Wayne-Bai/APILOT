
import pandas as pd

# Create two sample DataFrames
data1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
data2 = {'C': [7, 8, 9], 'D': [10, 11, 12]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Join columns of df1 with df2 based on their index
df_combined = df1.join(df2)

print(df_combined)
