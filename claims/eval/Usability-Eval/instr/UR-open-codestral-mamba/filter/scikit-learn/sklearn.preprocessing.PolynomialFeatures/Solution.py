from sklearn.preprocessing import PolynomialFeatures

# Let's assume we have a 2 dimensional feature matrix [a, b]
X = np.array([[2, 3], [4, 5], [6, 7]])

# We will generate a degree-2 polynomial feature matrix
polynomial_features = PolynomialFeatures(degree=2)
X_poly = polynomial_features.fit_transform(X)

print('Original Feature Matrix:', X)
print('Polynomial Features Matrix:', X_poly)
