
import numpy as np

def generate_polynomial_features(X, degree):
    n_samples, n_features = X.shape
    n_output_features = 1 + n_features + sum(range(n_features + 1, n_features + degree + 1))
    out = np.empty((n_samples, n_output_features), dtype=X.dtype)
    out[:, 0:n_features] = X
    if degree >= 2:
        index = n_features
        for d in range(2, degree + 1):
            for comb in combinations_with_replacement(range(n_features), d):
                out[:, index] = np.prod(X[:, comb], axis=1)
                index += 1
    return out
