import pandas as pd

# assume you have a dataframe called "df"
first_non_null = df.notnull().cumsum(axis=1).fillna(0).idxmax(axis=1)
print(first_non_null)
