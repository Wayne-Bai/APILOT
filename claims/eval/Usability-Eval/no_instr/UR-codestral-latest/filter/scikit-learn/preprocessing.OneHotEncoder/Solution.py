from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Assume x is the array containing categories
x = np.array([['dog'], ['cat'], ['bird'], ['cat'], ['dog']])

# Define the encoder
encoder = OneHotEncoder(sparse=False)

# Fit and transform the data
x_encoded = encoder.fit_transform(x)

print(x_encoded)
