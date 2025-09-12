import pandas as pd

# Sample DataFrame creation
data = {
    'Name': ['John', 'Anna', 'James', 'Linda', 'David'],
    'Age': [28, 22, 35, 32, 40]
}
df = pd.DataFrame(data)

# Returning the last n rows
n = 2
last_n_rows = df.tail(n)
print(last_n_rows)
