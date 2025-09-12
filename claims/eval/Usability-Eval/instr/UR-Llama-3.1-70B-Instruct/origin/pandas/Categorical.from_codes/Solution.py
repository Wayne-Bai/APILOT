# Import the pandas library
import pandas as pd

# Define categoricals from codes and categories
codes = [0, 1, 2, 0, 1, 2, 0, 1, 2]
categories = ['red', 'blue', 'green']

# Create a categorical
cat = pd.Categorical.from_codes(codes, categories)

# Print the categorical
print(cat)

# Define categoricals from dtype or list of categories
# Create a categorical
cat_dtype = pd.Series(['red', 'blue', 'green','red', 'blue', 'green'], dtype='category')

# Print the categorical
print(cat_dtype)

# You can also directly create a categorical from categories
cat_ary = pd.Categorical(['red','red', 'blue', 'blue', 'green', 'green'])
print(cat_ary)
