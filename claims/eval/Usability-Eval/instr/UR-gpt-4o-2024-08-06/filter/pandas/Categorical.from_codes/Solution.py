import pandas as pd

# Define the codes and corresponding categories
codes = [1, 2, 1, 3, 3, 2, 1]
categories = ['Small', 'Medium', 'Large']

# Create a Categorical dtype based on categories
categorical_type = pd.CategoricalDtype(categories=categories, ordered=True)

# Create a Series with categorical codes and convert it to the Categorical dtype
cat_series = pd.Series(pd.Categorical.from_codes(codes, dtype=categorical_type))

print(cat_series)
