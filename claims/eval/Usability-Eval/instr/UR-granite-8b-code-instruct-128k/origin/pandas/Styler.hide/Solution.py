import pandas as pd
# Create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
# Hide the entire index
df.index = pd.Index([], name=df.index.name)
# Hide the entire column headers
df.columns = pd.Index([], name=df.columns.name)
# Hide specific rows
df.loc[[0, 2], :] = pd.NA
# Hide specific columns
df.loc[:, ['A', 'C']] = pd.NA
print(df)
