import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=[0, 1, 2])

df2 = pd.DataFrame({
    'C': [7, 8, 9],
    'D': [10, 11, 12]
}, index=[0, 1, 2])

df3 = pd.DataFrame({
    'E': [13, 14, 15],
    'F': [16, 17, 18]
}, index=[0, 1, 2])

# Joining multiple DataFrames on index
result = pd.concat([df1, df2, df3], axis=1)

print(result)
