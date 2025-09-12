import pandas as pd

# Assuming df is your DataFrame and n is the number of rows you want to return
n = 5  # specify the number of rows
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6],
    'B': ['a', 'b', 'c', 'd', 'e', 'f']
})

# Return the first n rows
first_n_rows = df.iloc[:n]

print(first_n_rows)
