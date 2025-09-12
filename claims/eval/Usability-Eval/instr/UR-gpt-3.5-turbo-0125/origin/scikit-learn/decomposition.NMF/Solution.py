
import numpy as np

def nmf(X, n_components, max_iter=200):
    n_features = X.shape[1]
    W = np.random.rand(X.shape[0], n_components)
    H = np.random.rand(n_components, X.shape[1])
    
    for i in range(max_iter):
        # Update H
        H *= np.dot(W.T, X) / (np.dot(np.dot(W.T, W), H) + 1e-10)
        
        # Update W
        W *= np.dot(X, H.T) / (np.dot(W, np.dot(H, H.T)) + 1e-10)
    
    return W, H

# Example usage
X = np.array([[1, 2, 3], [4, 5, 6]])
n_components = 2
W, H = nmf(X, n_components)
print("W:\n", W)
print("H:\n", H)
