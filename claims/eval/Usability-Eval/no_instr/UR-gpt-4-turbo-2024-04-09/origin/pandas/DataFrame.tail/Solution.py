import pandas as pd

# Sample DataFrame to demonstrate
data = {
    'Name': ['John', 'Anna', 'James', 'Linda', 'Emily'],
    'Age': [28, 22, 35, 32, 15],
    'Country': ['USA', 'UK', 'USA', 'Canada', 'Australia']
}

df = pd.DataFrame(data)

# Get the last n rows from the DataFrame
n = 2
last_n_rows = df.tail(n)
print(last_n_rows)
