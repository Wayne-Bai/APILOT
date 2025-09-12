import pandas as pd

# Sample data
data1 = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

data2 = {
    'A': [1, 2, 3],
    'B': [4, 6, 9],
    'D': [10, 11, 12]
}

# Create DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Compare DataFrames and show differences
differences = pd.concat([df1, df2]).drop_duplicates(keep=False)
print(differences)
