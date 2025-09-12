import pandas as pd

# Creating a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': ['a', 'b', 'c', 'd']})

# Create a mapping dictionary
mapping = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# Mapping the values in column 'B' using the mapping
df['B'] = df['B'].map(mapping)
