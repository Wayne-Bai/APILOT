
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Generate polynomial and interaction features
def generate_polynomial_features(X, degree):
    poly = PolynomialFeatures(degree=degree)
    return poly.fit_transform(X)
