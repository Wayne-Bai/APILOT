
import pandas as pd

# create a sample dataset
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})

# compute the sum of group values for each row in the dataframe
group_sums = df.groupby('A').sum()

# print the results
print(group_sums)
