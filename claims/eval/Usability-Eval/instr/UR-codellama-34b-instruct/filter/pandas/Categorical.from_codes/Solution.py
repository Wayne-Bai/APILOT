import pandas as pd

# Create a sample DataFrame with some data
df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3]})

# Define the categories and codes for the categorical column
categories = ['a', 'b', 'c']
codes = [0, 1, 2]

# Create a new categorical column with the defined categories and codes
df['C'] = pd.Categorical(values=df['A'], categories=categories, codes=codes)

print(df)
