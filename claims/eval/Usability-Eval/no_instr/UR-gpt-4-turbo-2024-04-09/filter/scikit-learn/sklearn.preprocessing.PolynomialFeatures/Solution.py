from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Example data
X = np.array([[1, 2], [3, 4], [5, 6]])

# Create a PolynomialFeatures object with degree 2
poly = PolynomialFeatures(degree=2)

# Transform the data to create polynomial features
X_poly = poly.fit_transform(X)

print(X_poly)
