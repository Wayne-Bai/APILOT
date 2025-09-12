import pandas as pd

# Create a series of strings representing category codes
codes = ['A', 'B', 'C']

# Create a series of strings representing category names
categories = ['Category A', 'Category B', 'Category C']

# Create a categorical type from the codes and categories
cat_type = pd.api.types.CategoricalDtype(codes, categories)
