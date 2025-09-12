from sklearn.preprocessing import PolynomialFeatures

# Assuming X is your feature matrix
X = [[1], [2], [3], [4]]

# Define the degree of polynomial features
degree = 2

# Create a polynomial features object
poly = PolynomialFeatures(degree=degree, include_bias=False)

# Fit and transform the X data
X_poly = poly.fit_transform(X)

print(X_poly)
