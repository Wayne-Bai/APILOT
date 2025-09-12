
import pandas as pd

# create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})

# compute the min value of each group in column A
result = df.groupby('A').min()

print(result)
