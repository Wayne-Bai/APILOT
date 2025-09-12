from sklearn.preprocessing import PolynomialFeatures

# Assuming X is your input data
X = ...

# Define the degree of polynomial features
degree = 2

# Generate polynomial and interaction features
poly = PolynomialFeatures(degree=degree, include_bias=False)
X_poly = poly.fit_transform(X)

# Print the new feature matrix
print(X_poly)
