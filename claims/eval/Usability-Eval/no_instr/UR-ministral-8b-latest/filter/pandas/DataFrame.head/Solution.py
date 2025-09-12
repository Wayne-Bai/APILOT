import pandas as pd

def get_first_n_rows(df, n):
    return df.head(n)

# Example usage:
# assuming `df` is a pd.DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': ['a', 'b', 'c', 'd', 'e']
})

n = 3
first_n_rows = get_first_n_rows(df, n)
print(first_n_rows)
