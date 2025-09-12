import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Create a random input matrix
X = np.random.rand(10, 2)

# Initialize a PolynomialFeatures object with specified degree
poly = PolynomialFeatures(degree=2)

# Generate the new feature matrix
X_poly = poly.fit_transform(X)

# Print the original and polynomial feature matrices
print("Original feature matrix:")
print(X)
print("\nPolynomial feature matrix:")
print(X_poly)
