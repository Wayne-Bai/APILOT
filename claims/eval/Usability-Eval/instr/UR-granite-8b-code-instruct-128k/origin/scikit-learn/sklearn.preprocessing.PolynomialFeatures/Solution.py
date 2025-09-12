from sklearn.preprocessing import PolynomialFeatures

def generate_polynomial_and_interaction_features(X, degree):
    poly = PolynomialFeatures(degree=degree, interaction_only=False, include_bias=True)
    return poly.fit_transform(X)
