from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Let's assume you have a 2D feature matrix X
X = np.array([[a, b] for a, b in zip(range(10), range(10))])

# Create a PolynomialFeatures object with degree 2
poly = PolynomialFeatures(2)

# Generate the polynomial features
X_poly = poly.fit_transform(X)

# Print the original and the new feature matrix
print("Original features:\n", X)
print("Polynomial features:\n", X_poly)
