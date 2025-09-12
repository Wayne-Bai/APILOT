from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Example input data
X = np.array([[2, 3],
              [4, 5],
              [6, 7]])

# Specify the degree of polynomial features
degree = 2

# Create an instance of PolynomialFeatures with the desired degree
poly = PolynomialFeatures(degree)

# Transform the input data to include polynomial and interaction features
X_poly = poly.fit_transform(X)

# Output the transformed feature matrix
print(X_poly)
