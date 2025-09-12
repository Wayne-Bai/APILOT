from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Create an instance of PolynomialFeatures
poly = PolynomialFeatures(degree=2)

# Create a new feature matrix consisting of all polynomial combinations of the features with degree less than or equal to the specified degree
X = np.arange(9).reshape(3, 3)
print(poly.fit_transform(X))
