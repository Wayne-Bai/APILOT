import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': ['a', 'b', 'c', 'd']
}
df = pd.DataFrame(data)

# Mapping dictionary
mapping = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

# Applying the mapping to column 'A'
df['A'] = df['A'].map(mapping)

print(df)
