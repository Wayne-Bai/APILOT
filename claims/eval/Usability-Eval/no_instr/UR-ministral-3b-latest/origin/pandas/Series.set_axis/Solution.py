import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Assigning an index
new_index = ['a', 'b', 'c']

df.index = new_index

print(df)
