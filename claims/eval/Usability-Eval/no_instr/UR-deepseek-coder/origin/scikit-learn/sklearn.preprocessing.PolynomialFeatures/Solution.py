import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Example input data
X = np.array([[1, 2], [3, 4]])

# Generate polynomial features up to degree 2
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

print(X_poly)
