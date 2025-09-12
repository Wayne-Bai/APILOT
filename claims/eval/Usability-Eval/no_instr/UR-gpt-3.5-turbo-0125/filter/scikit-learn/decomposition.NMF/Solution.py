
import numpy as np

def my_nmf(X, n_components):
    np.random.seed(0)
    n_samples, n_features = X.shape

    W = np.abs(np.random.rand(n_samples, n_components))
    H = np.abs(np.random.rand(n_components, n_features))

    for i in range(200):
        # Update W
        WH = np.dot(W, H) + 1e-9
        W *= np.dot(X / WH, H.T) / np.sum(H, axis=1)

        # Update H
        WH = np.dot(W, H) + 1e-9
        H *= np.dot(W.T, X / WH) / np.sum(W, axis=0)

    return W, H
