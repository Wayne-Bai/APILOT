import pandas as pd

def get_last_n_rows(df, n):
    return df.tail(n)

# Create a sample dataframe
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
df = pd.DataFrame(data)

# Get the last 2 rows
last_two_rows = get_last_n_rows(df, 2)
print(last_two_rows)
