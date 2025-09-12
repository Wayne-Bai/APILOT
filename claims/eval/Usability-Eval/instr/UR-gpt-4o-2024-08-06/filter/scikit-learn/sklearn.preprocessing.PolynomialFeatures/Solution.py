import numpy as np

class PolynomialFeaturesCustom:
    def __init__(self, degree=2):
        self.degree = degree

    def fit_transform(self, X):
        n_samples, n_features = X.shape
        combinations = self._generate_combinations(n_features)
        n_output_features = len(combinations)
        X_new = np.empty((n_samples, n_output_features), dtype=X.dtype)
        
        for i, comb in enumerate(combinations):
            X_new[:, i] = np.prod(X[:, comb], axis=1)
        
        return X_new

    def _generate_combinations(self, n_features):
        from itertools import combinations_with_replacement
        comb = [()]

        for degree in range(1, self.degree + 1):
            comb.extend(combinations_with_replacement(range(n_features), degree))
        
        return comb

# Example usage
X = np.array([[0, 1], [2, 3], [4, 5]])
poly = PolynomialFeaturesCustom(degree=2)
X_poly = poly.fit_transform(X)
print(X_poly)
