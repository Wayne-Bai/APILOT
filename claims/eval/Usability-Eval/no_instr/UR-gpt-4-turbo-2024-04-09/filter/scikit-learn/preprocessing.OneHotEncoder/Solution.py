from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Example categorical array
data = np.array([['red'], ['blue'], ['green'], ['blue']])

# Creating the OneHotEncoder object
encoder = OneHotEncoder(sparse=False)

# Transforming the data
encoded_data = encoder.fit_transform(data)

print(encoded_data)
