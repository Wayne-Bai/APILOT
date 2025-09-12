
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Create example categorical data
data = np.array([['red'], ['blue'], ['green'], ['yellow']])

# Initialize OneHotEncoder
encoder = OneHotEncoder()

# Fit and transform the data
encoded_data = encoder.fit_transform(data).toarray()

print(encoded_data)
