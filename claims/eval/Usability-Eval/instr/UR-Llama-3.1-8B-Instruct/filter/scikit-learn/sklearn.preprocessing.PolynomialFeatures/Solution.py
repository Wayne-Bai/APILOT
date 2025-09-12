# Import necessary libraries from scikit-learn
from sklearn.preprocessing import PolynomialFeatures
from sklearn import datasets
import numpy as np

# Generate a sample dataset
X, y = datasets.load_diabetes(return_X_y=True)

# Initialize the degree
degree = 2

# Initialize the polynomial feature object
poly_features = PolynomialFeatures(degree=degree)

# Fit the polynomial feature object to the training data
poly_features.fit(X)

# Generate polynomial and interaction features
X_poly = poly_features.transform(X)

# Print the shape of the original and polynomial feature matrices
print("Original feature matrix shape:", X.shape)
print("Polynomial feature matrix shape:", X_poly.shape)
