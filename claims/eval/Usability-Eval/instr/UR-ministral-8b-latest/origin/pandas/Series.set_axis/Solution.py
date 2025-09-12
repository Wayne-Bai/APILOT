import pandas as pd

# Sample data
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
}
df = pd.DataFrame(data)

# Assigning customized index
df.index = ['a', 'b', 'c', 'd']

print(df)
