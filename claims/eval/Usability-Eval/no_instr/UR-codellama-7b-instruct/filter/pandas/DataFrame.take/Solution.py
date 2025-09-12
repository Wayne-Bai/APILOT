import pandas as pd

# create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'C': [9, 10, 11, 12]})

# print the elements in positional indices along an axis
print(df.iloc[0])  # prints the first row of the dataframe
print(df.iloc[[0, 3]])  # prints the first and fourth rows of the dataframe
