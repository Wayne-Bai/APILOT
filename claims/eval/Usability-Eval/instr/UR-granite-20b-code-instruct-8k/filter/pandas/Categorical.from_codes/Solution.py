
import pandas as pd

# Define codes and categories
codes = [0, 1, 2, 0, 2, 1]
categories = ['A', 'B', 'C']

# Create Categorical type from codes and categories
categorical_series = pd.Categorical(codes, categories=categories)

# Display the Categorical type
print(categorical_series)
