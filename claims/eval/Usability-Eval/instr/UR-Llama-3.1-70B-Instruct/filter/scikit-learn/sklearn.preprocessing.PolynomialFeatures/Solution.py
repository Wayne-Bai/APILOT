# Importing necessary libraries
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Creating a simple dataset
X = np.array([[1, 2], [3, 4]])

# Creating an instance of PolynomialFeatures with the desired degree
poly = PolynomialFeatures(degree=2)

# Fitting the feature matrix and transforming it into polynomial features
X_poly = poly.fit_transform(X)

# Displaying the initial and resulting feature matrices
print("Initial feature matrix:")
print(X)
print("\nPolynomial feature matrix (degree = 2):")
print(X_poly)
