import pandas as pd

# Define the categories and codes
categories = ['Low', 'Medium', 'High']
codes = [1, 2, 3]

# Create a dictionary to map codes to categories
category_map = dict(zip(codes, categories))

# Create a pandas Series with the codes
codes_series = pd.Series(codes)

# Convert the Series to a Categorical type with the defined categories
# The categories argument sets the categories and order (if interested), and the codes argument maps the codes to the categories
categorical_series = pd.Categorical(codes_series, categories=categories, ordered=True)

# Optionally, create a DataFrame to visualize the mapping
df = pd.DataFrame({'Codes': codes_series, 'Categories': categorical_series})
print(df)
