from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Create a sample categorical data
categorical_data = np.array(['cat', 'dog', 'bird', 'cat', 'bird', 'dog', 'cat'])

# Initialize the OneHotEncoder
encoder = OneHotEncoder(sparse=False)

# Fit and transform the categorical data
one_hot_data = encoder.fit_transform(categorical_data.reshape(-1, 1))

print(one_hot_data)
