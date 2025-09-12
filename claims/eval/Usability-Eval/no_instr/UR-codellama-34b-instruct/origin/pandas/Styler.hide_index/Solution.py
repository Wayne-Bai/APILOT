
import pandas as pd

# create a sample dataframe with an index
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])

# hide the entire index
print(df)
#     A  B
# a  1  4
# b  2  5
# c  3  6

# hide specific keys in the index using the .loc[] method
print(df.loc[['a', 'c']])
#     A  B
# a  1  4
# c  3  6
