from sklearn.preprocessing import PolynomialFeatures

def generate_polynomial_features(X, degree):
    """
    Generate polynomial and interaction features from the input features.

    Parameters:
    X (array-like): The input features, shape (n_samples, n_features).
    degree (int): The degree of the polynomial features to generate.

    Returns:
    X_poly (array-like): The features with polynomial and interaction terms.
    """
    poly = PolynomialFeatures(degree, include_bias=False)
    X_poly = poly.fit_transform(X)
    return X_poly
