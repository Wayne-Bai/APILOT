import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Return the first n rows
n = 3
first_n_rows = df.head(n)

print(first_n_rows)
