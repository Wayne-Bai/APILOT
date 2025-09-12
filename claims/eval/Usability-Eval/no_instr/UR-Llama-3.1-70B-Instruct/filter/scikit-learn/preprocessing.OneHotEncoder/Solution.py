# Import necessary libraries from scikit-learn
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Sample categorical data
data = np.array([
    ['Male', 'USA', 'Student'],
    ['Female', 'Canada', 'Engineer'],
    ['Male', 'USA', 'Engineer'],
    ['Female', 'Canada', 'Student'],
])

# Create an instance of the OneHotEncoder class
encoder = OneHotEncoder(sparse=False)

# Fit the encoder to the data and transform it into a one-hot encoded array
encoded_data = encoder.fit_transform(data)

# Print the encoded data
print("Encoded Data:")
print(encoded_data)

# Print the categories for each feature
print("\nCategories for each feature:")
for i, categories in enumerate(encoder.categories_):
    print(f"Feature {i}: {categories}")
