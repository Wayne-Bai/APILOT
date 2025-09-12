import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df)
#      A  B
#  0  1  4
#  1  2  5
#  2  3  6

# Assign a new index to the dataframe
new_index = ['a', 'b', 'c']
df.index = new_index
print(df)
#      A  B
# a  1  4
# b  2  5
# c  3  6
