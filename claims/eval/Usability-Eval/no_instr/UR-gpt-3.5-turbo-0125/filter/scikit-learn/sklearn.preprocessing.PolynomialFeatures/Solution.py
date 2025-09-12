
import numpy as np

def generate_polynomial_features(X, degree):
    n_samples, n_features = X.shape
    new_features = []
    
    for i in range(1, degree + 1):
        for j in range(n_features):
            new_feature = X[:, j]**i
            new_features.append(new_feature)
    
    for i in range(n_features):
        for j in range(i+1, n_features):
            new_feature = X[:, i] * X[:, j]
            new_features.append(new_feature)
    
    return np.column_stack(new_features)
