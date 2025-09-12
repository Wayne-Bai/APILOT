from sklearn.preprocessing import PolynomialFeatures

# Let's consider X as the input feature matrix
# degree is the degree of the polynomial features
degree = 2

poly = PolynomialFeatures(degree=degree, include_bias=False)

# Generating polynomial and interaction features
X_poly = poly.fit_transform(X)
