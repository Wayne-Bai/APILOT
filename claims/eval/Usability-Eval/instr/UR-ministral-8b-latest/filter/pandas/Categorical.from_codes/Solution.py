import pandas as pd

# Sample data
data = {'Code': [1, 2, 3, 4],
        'Categories': ['A', 'B', 'A', 'B']}

# Create a DataFrame
df = pd.DataFrame(data)

# Make 'Code' as Categorical type
df['Code'] = df['Code'].astype('category')

# Make 'Categories' as categorical type
df['Categories'] = df['Categories'].cat.categories = pd.Categorical(df['Categories'])

print(df)
