
import pandas as pd

# Creating DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})

# Joining columns of df1 with df2 on index
result = df1.join(df2)

# Displaying the result
print(result)
