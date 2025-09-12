import pandas as pd

# Assuming df is your DataFrame and n is the number of rows you want to return
n = 5
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10]
})

# Return the last n rows
last_n_rows = df.tail(n)
print(last_n_rows)
