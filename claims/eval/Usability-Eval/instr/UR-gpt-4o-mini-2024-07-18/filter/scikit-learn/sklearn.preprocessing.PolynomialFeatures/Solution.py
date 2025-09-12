import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Sample input data
X = np.array([[2, 3],
              [1, 5],
              [4, 2]])

# Create an instance of PolynomialFeatures
degree = 2
poly = PolynomialFeatures(degree)

# Generate polynomial features
X_poly = poly.fit_transform(X)

print(X_poly)
