from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Example data: a 2D array with categorical features
data = np.array([
    ['red', 'small'],
    ['blue', 'medium'],
    ['green', 'large']
])

# Initialize the OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)

# Fit and transform the data to one-hot encode it
encoded_data = encoder.fit_transform(data)

# Print the transformed array
print(encoded_data)

# Print the category names for each feature
print(encoder.categories_)
