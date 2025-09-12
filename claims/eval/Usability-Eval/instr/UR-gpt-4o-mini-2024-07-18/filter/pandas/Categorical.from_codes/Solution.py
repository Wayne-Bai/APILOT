import pandas as pd

# Sample data
codes = [1, 2, 3, 1, 2]
categories = ['A', 'B', 'C']

# Create a Categorical type
cat_type = pd.CategoricalDtype(categories=categories, ordered=True)

# Convert the codes to a Categorical type
categorical_data = pd.Series(codes, dtype=cat_type)

# Display the result
print(categorical_data)
