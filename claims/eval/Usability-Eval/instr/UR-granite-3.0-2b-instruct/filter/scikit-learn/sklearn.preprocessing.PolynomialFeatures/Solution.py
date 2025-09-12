from sklearn.preprocessing import PolynomialFeatures

class PolyFeatures:
    def __init__(self, degree):
        self.degree = degree

    def fit_transform(self, X):
        self.poly = PolynomialFeatures(degree=self.degree, include_bias=False)
        return self.poly.fit_transform(X)

    def get_features(self):
        return self.poly.get_feature_names_out()

# Usage
poly = PolyFeatures(degree=2)
X = [[1, 2], [3, 4], [5, 6]]
X_poly = poly.fit_transform(X)
print("Polynomial Features:")
print(X_poly)
print("\nFeatures:")
print(poly.get_features())
