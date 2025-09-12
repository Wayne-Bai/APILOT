from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Sample categorical data
data = np.array([['red'], ['blue'], ['green'], ['red']])

# Create an instance of OneHotEncoder
encoder = OneHotEncoder(sparse=False)

# Fit and transform the data
one_hot_encoded = encoder.fit_transform(data)

print(one_hot_encoded)
