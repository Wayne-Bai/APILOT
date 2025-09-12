from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Suppose we have the following categorical feature
X = np.array([['male'], ['female'], ['female'], ['male'], ['male']])

# Create a OneHotEncoder object
encoder = OneHotEncoder(sparse=False)

# Convert categorical feature into one-hot encoded array
X_encoded = encoder.fit_transform(X)

print(X_encoded)
