import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
}

df = pd.DataFrame(data)

# Assigning a custom index
df.index = ['a', 'b', 'c', 'd']

print(df)
