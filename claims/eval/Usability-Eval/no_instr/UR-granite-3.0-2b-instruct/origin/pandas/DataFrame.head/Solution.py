import pandas as pd

# Assuming df is your DataFrame and n is the number of rows you want to return
n = 5
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
})

# Return the first n rows
first_n_rows = df.head(n)

print(first_n_rows)
