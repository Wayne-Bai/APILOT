
import pandas as pd

# Create a sample dataframe
data = {'A': ['a', 'b', 'c', 'a', 'b', 'c'],
        'B': [1, 2, 3, 4, 5, 6]}
df = pd.DataFrame(data)

# Map values using a mapping dictionary
mapping = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
df['A_mapped'] = df['A'].map(mapping)

print(df)
