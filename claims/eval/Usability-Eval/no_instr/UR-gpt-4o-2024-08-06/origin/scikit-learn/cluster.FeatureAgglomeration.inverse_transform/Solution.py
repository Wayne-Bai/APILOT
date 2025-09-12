import numpy as np
from sklearn.preprocessing import StandardScaler

# Sample data: Assume this is your feature matrix
X = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0],
              [7.0, 8.0, 9.0]])

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit the scaler to the data and transform it
X_scaled = scaler.fit_transform(X)

# Assume you have transformed data that you want to inverse transform
# For this example, let's inverse the transformation of the first row
transformed_vector = X_scaled[0]

# Perform the inverse transformation to get back to the original feature space
original_vector = scaler.inverse_transform(transformed_vector.reshape(1, -1))

# Flatten the result to get a single vector
original_vector_flat = original_vector.flatten()

print("Original vector:", original_vector_flat)
