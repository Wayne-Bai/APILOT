import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Sample input for demonstration
X = np.array([[9, 2], [12, -3], [5, 8]])

# Set the degree for polynomial transformations
degree = 2

# Create the polynomial feature transformer
poly = PolynomialFeatures(degree)

# Fit the transformer and transform the data
X_poly = poly.fit_transform(X)

print('Original data:')
print(X)

print('\nPolynomial features:')
print(poly.transform(X))
