import pandas as pd

# Sample DataFrame
data = {
    'column1': [1, 2, 3, 4, 5],
    'column2': ['a', 'b', 'c', 'd', 'e']
}
df = pd.DataFrame(data)

# Number of rows to return
n = 3

# Return the first n rows
first_n_rows = df.head(n)

first_n_rows
