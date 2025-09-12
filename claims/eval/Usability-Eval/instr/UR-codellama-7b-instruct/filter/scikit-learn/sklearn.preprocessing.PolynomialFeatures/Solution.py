from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Define the number of features and the degree of the polynomial
n_features = 2
degree = 2

# Generate a set of random data
X = np.random.rand(10, n_features)

# Initialize the PolynomialFeatures class with the desired degree
poly = PolynomialFeatures(degree=degree)

# Fit the polynomial features to the data
poly_transformed = poly.fit_transform(X)

# Print the generated features
print(poly_transformed)
