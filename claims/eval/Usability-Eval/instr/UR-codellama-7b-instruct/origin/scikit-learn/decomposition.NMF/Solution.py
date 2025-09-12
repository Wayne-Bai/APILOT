
import numpy as np
from sklearn.utils import check_array
from sklearn.preprocessing import normalize

def nmf(X):
    """
    Non-negative Matrix Factorization (NMF)
    Input: X - non-negative matrix of shape (n_samples, n_features)
    Output: W - non-negative matrix of shape (n_components, n_features)
            H - non-negative matrix of shape (n_components, n_samples)
    """
    # Check the input
    X = check_array(X, accept_sparse=True)
    if not np.all(X >= 0):
        raise ValueError("The input matrix must contain only non-negative values.")
    
    # Perform NMF
    W = normalize(np.random.randn(n_components, n_features), axis=1)
    H = normalize(np.random.randn(n_components, n_samples), axis=1)
    
    for i in range(max_iter):
        # Compute the reconstruction error
        reconstructed_X = W @ H
        error = np.linalg.norm(reconstructed_X - X) / np.sqrt(n_samples)
        
        # Update W and H
        if i % 2 == 0:
            H += (X - reconstructed_X @ np.transpose(W)) / n_components
            W += (reconstructed_X - X @ np.transpose(H)) / n_features
        else:
            W += (X - reconstructed_X @ np.transpose(H)) / n_components
            H += (reconstructed_X - X @ np.transpose(W)) / n_samples
    
    return W, H
