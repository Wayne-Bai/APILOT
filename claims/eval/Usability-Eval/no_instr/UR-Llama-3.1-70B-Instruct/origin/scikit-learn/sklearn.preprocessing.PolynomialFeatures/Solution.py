# Importing necessary libraries
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Create a sample feature matrix
X = np.array([[1, 2], [3, 4]])

# Create an instance of PolynomialFeatures
poly = PolynomialFeatures(degree=2)

# Generate polynomial and interaction features
X_poly = poly.fit_transform(X)

print("Original Feature Matrix:")
print(X)
print("\nPolynomial and Interaction Features:")
print(X_poly)
