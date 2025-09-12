from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Example input data
X = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Specify the degree
degree = 2

# Generate polynomial features
poly = PolynomialFeatures(degree=degree)
X_poly = poly.fit_transform(X)

print(X_poly)
