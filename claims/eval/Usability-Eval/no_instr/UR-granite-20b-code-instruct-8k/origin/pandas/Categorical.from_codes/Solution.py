import pandas as pd

# Define the codes and categories
codes = [1, 2, 3, 4, 5]
categories = ['A', 'B', 'C', 'D', 'E']

# Create a Categorical type from codes and categories
categorical_series = pd.Series(codes, dtype='category', categories=categories)

# Display the Categorical type
print(categorical_series)

