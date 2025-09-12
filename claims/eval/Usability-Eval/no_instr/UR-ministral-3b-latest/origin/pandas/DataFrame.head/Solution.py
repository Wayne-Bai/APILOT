import pandas as pd

# Assuming you have the DataFrame `df`
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': ['a', 'b', 'c', 'd']
})

first_n_rows = df.head(n=3)  # returns the first 3 rows
print(first_n_rows)
