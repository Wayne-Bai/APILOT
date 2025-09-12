import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': ['a', 'b', 'c', 'd', 'e']
}

df = pd.DataFrame(data)

# Function to return the first n rows
def get_first_n_rows(dataframe, n):
    return dataframe.head(n)

# Example usage
n = 3
first_n_rows = get_first_n_rows(df, n)
print(first_n_rows)
