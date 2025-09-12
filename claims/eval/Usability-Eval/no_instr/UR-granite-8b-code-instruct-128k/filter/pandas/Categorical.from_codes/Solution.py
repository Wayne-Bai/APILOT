import pandas as pd

# Assuming you have a list of codes and a list of categories
codes = [1, 2, 3, 4, 5]
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']

# Create a Categorical type from codes and categories
cat_type = pd.Categorical(codes, categories)

# Print the Categorical type
print(cat_type)
