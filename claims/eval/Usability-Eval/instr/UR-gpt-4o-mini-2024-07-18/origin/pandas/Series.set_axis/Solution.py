import pandas as pd

# Sample data
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Assigning desired index to the given axis (rows)
desired_index = ['a', 'b', 'c']
df.index = desired_index

print(df)
