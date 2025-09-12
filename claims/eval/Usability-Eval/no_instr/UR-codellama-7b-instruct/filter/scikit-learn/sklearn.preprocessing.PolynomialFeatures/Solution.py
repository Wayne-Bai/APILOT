
from sklearn.preprocessing import PolynomialFeatures

# Generate a new feature matrix consisting of all polynomial combinations of the features with degree less than or equal to the specified degree
def generate_polynomial_features(data, degree):
    poly_features = PolynomialFeatures(degree=degree)
    return poly_features.fit_transform(data)
