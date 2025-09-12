
import numpy as np

def NMF(X, n_components, max_iter=200):
    # Initialize matrices W and H with random values
    W = np.random.rand(X.shape[0], n_components)
    H = np.random.rand(n_components, X.shape[1])

    for i in range(max_iter):
        # Update matrix H
        H *= (W.T @ X) / (W.T @ W @ H + 1e-9)
        
        # Update matrix W
        W *= (X @ H.T) / (W @ H @ H.T + 1e-9)

    return W, H

# Example usage
X = np.random.rand(100, 50)  # Example input matrix X
n_components = 5
W, H = NMF(X, n_components)
