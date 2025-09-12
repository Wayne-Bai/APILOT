from sklearn.preprocessing import PolynomialFeatures

# Let's assume we have a dataset X
# Each row is an example and each column is a feature
X = [[2, 3], [1, 4], [5, 2]]

# Initialize PolynomialFeatures object
poly = PolynomialFeatures(degree=2, include_bias=False)

# Generate polynomial and interaction features
X_poly = poly.fit_transform(X)

print(X_poly)
