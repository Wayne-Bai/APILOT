import pandas as pd

# Sample DataFrame creation
data = {
    'A': [1, 2, None, 4],
    'B': [None, None, 'Hello', 'World'],
    'C': [None, 2.5, 3.5, None]
}

df = pd.DataFrame(data)

# Compute the last non-null entry of each column
last_non_null = df.apply(lambda x: x.last_valid_index() if x.last_valid_index() is not None else None)
last_values = df.lookup(last_non_null.index, last_non_null)

# Creating a result DataFrame
result = pd.DataFrame(last_values, index=last_non_null.index, columns=['Last Non-Null Entry'])

print(result)
