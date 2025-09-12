import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Assuming X is your feature matrix
X = np.array([[2, 3], [0, 1], [2, 2], [3, 3]])  # Example feature matrix

# Degree of polynomial features to be generated
degree = 2

# Create the PolynomialFeatures transformer
poly = PolynomialFeatures(degree=degree)

# Generate the new feature matrix with polynomial and interaction features
X_poly = poly.fit_transform(X)

print("Original feature matrix:")
print(X)
print("\nPolynomial feature matrix:")
print(X_poly)
