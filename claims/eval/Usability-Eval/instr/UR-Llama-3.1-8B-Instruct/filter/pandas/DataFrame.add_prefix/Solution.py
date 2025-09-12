# Importing pandas library
import pandas as pd

# Creating a sample Series
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# Prefixing the row labels with 'label_'
s = s.rename_axis('label_')

print('Prefixing labels for Series:')
print(s)

# Creating a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}, index=['p', 'q', 'r'])

# Prefixing the column labels with 'column_'
df.columns = ['column_' + c for c in df.columns]

print('\nPrefixing labels for DataFrame:')
print(df)

# Creating another DataFrame
df2 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}, index=['p', 'q', 'r'])

# Prefixing the column labels with 'column_' using rename method
df2 = df2.rename(columns=lambda x: 'column_' + x)

print('\nPrefixing labels for DataFrame using rename method:')
print(df2)
