import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10]
}
df = pd.DataFrame(data)

# Function to return the first n rows of the dataframe
def first_n_rows(dataframe, n):
    return dataframe.head(n)

# Example usage: Get the first 3 rows of the dataframe
first_rows = first_n_rows(df, 3)
print(first_rows)
