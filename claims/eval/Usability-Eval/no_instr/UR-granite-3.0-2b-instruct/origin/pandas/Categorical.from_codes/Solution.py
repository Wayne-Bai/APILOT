import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'code': ['A', 'B', 'C', 'A', 'B', 'C'],
    'category': ['cat1', 'cat2', 'cat3', 'cat1', 'cat2', 'cat3']
})

# Create a Categorical type from the 'code' column
df['code'] = pd.Categorual(df['code'])

# Set the 'code' column as the DataFrame's dtype
df.dtype['code'] = 'category'
