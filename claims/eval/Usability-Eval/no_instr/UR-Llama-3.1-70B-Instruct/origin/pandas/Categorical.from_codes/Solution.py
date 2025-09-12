# Importing pandas library
import pandas as pd

# Define the codes and corresponding categories
codes = [0, 1, 1, 0, 2, 1]
categories = ['A', 'B', 'C']

# Create a Categorical type from codes and categories
categorical = pd.Categorical.from_codes(codes, categories)

# Print the Categorical type
print(categorical)

# Define the data type of the category
dtype = pd.CategoricalDtype(categories=['A', 'B', 'C'])

# Create a Categorical type from data and dtype
categorical_dtype = pd.Categorical([0, 1, 1, 0, 2, 1], dtype=dtype)

# Print the Categorical type
print(categorical_dtype)

# To avoid using deprecated code, ensure that categories are always in the order specified in the.cat.categories attribute:
data = pd.Series(['A', 'B', 'C', 'A', 'B', 'C'])
categorical_ordered = data.astype(pd.CategoricalDtype(list('ABC'), ordered=True))

print(categorical_ordered)
