
from sklearn import linear_model
import numpy as np

def generate_sparse_coded_signal(n_features, n_components, n_samples, n_nonzero_coefs):
    D = np.random.randn(n_features, n_components)
    X = np.zeros((n_components, n_samples))
    for i in range(n_samples):
        nonzero_indices = np.random.choice(n_components, n_nonzero_coefs, replace=False)
        X[nonzero_indices, i] = np.random.randn(n_nonzero_coefs)
    
    Y = np.dot(D, X)
    
    return Y
