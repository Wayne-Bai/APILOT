import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': ['cat', 'dog', 'cat', 'bird', 'dog', 'cat'],
    'B': ['small', 'large', 'small', 'medium', 'large', 'small']
})

# Define the categories
categories = ['cat', 'dog', 'bird']

# Create a Categorical type from codes and categories
df['A'] = pd.CategorualDtype(categories=categories).annotate(df['A'])
df['B'] = pd.CategoricalDtype(categories=categories).annotate(df['B'])

# Print the DataFrame
print(df)
