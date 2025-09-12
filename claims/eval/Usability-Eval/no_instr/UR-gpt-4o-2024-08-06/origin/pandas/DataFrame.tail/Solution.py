import pandas as pd

# Assuming df is your DataFrame and n is the number of rows you want to retrieve
def get_last_n_rows(df, n):
    return df.tail(n)

# Example usage:
# data = {'column1': [1, 2, 3, 4, 5], 'column2': ['a', 'b', 'c', 'd', 'e']}
# df = pd.DataFrame(data)
# last_rows = get_last_n_rows(df, 3)
# print(last_rows)
