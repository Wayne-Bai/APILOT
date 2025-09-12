
import pandas as pd

# Sample input data
data = {'A': ['apple', 'banana', 'cherry'], 'B': [1, 2, 3]}
df = pd.DataFrame(data)

# Define a mapping dictionary
mapping = {'apple': 5, 'banana': 10, 'cherry': 15}

# Map values using the input mapping
df['A'] = df['A'].map(mapping)

print(df)
