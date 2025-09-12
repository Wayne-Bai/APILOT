from sklearn.preprocessing import PolynomialFeatures
import numpy as np

X = np.arange(9).reshape(3, 3)
poly = PolynomialFeatures(2)

# Generate polynomial and interaction features
X_poly = poly.fit_transform(X)

print(X_poly)
