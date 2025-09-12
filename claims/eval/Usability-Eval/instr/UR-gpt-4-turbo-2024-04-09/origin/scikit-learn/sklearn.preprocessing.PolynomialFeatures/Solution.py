from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Example data
X = np.array([[1, 2], [3, 4], [5, 6]])

# Create a Polynomial Features transformer for degree 2
poly_transformer = PolynomialFeatures(degree=2)

# Fit and transform the data
X_poly = poly_transformer.fit_transform(X)

print(X_poly)
