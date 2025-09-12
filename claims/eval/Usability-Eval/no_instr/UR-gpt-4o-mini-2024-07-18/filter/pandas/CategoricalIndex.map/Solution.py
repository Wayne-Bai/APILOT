import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Input mapping or function
mapping = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

# Map values using the mapping
df['B'] = df['A'].map(mapping)

print(df)
