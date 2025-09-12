import pandas as pd

# Define the codes and categories
codes = ['A', 'B', 'C', 'D']
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']

# Create a Categorical type
dtype = pd.CategoricalDtype(categories=categories, ordered=False)

# Make a DataFrame with the codes and categories
df = pd.DataFrame({
    'Code': codes,
    'Category': pd.Categorical(codes, dtype=dtype)
})
