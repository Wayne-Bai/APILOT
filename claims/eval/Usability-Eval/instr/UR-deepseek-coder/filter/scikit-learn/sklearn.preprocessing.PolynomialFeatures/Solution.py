import numpy as np

def polynomial_features(X, degree):
    n_samples, n_features = X.shape
    combinations = [np.arange(n_features)]
    
    for d in range(2, degree + 1):
        new_combinations = []
        for combination in combinations:
            for feature in range(n_features):
                if feature not in combination:
                    new_combination = np.append(combination, feature)
                    new_combinations.append(new_combination)
        combinations.extend(new_combinations)
    
    poly_features = []
    for combination in combinations:
        poly_features.append(np.prod(X[:, combination], axis=1))
    
    poly_features = np.column_stack(poly_features)
    return poly_features

# Example usage
X = np.array([[1, 2], [3, 4]])
degree = 2
poly_X = polynomial_features(X, degree)
print(poly_X)
