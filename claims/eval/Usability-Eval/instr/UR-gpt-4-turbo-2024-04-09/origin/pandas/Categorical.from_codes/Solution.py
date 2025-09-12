import pandas as pd

# Given categories and codes
categories = ['red', 'blue', 'green']
codes = [0, 1, 2, 0, 1]

# Creating a categorical type
categorical_data = pd.Categorical.from_codes(codes, categories)

print(categorical_data)
