
import pandas as pd

# Specify codes and corresponding categories
codes = [0, 1, 2, 1, 0]
categories = ['A', 'B', 'C']

# Create a categorical type using codes and categories
cat_type = pd.Categorical.from_codes(codes, categories)

# Printing the categorical type
print(cat_type)
