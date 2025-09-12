import pandas as pd

# Example DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 30, 22, 29, 25]
}

df = pd.DataFrame(data)

# Specify the number of last rows you want to return
n = 2

# Return the last n rows
last_n_rows = df.iloc[-n:]
print(last_n_rows)
