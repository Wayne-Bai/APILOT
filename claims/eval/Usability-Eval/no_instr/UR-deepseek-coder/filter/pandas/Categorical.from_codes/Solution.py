import pandas as pd

# Example codes and categories
codes = [0, 1, 2, 0, 1, 2]
categories = ['A', 'B', 'C']

# Create a Categorical type
cat = pd.Categorical.from_codes(codes, categories=categories)

# Display the Categorical type
print(cat)
