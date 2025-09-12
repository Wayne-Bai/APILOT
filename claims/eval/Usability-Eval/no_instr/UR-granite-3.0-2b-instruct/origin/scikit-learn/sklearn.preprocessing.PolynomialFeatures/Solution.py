from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Assuming X is the input feature matrix
# and degree is the degree of the polynomial features

# Initialize PolynomialFeatures with the specified degree
poly = PolynomialFeatures(degree=2)

# Fit and transform the feature matrix
X_poly = poly.fit_transform(X)

# Print the new feature matrix
print(X_poly)
