import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Example input: 2D array with sample data
X = np.array([[2, 3], [1, 1], [4, 1]])

# Set the degree parameter
degree = 2

# Instantiate the PolynomialFeatures transformer
poly = PolynomialFeatures(degree=degree, include_bias=False)

# Fit and transform the data
X_poly = poly.fit_transform(X)

print(X_poly)
