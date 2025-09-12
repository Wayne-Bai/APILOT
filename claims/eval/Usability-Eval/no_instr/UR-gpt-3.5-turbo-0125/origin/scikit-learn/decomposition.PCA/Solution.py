
import numpy as np

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None

    def fit(self, X):
        # Center the data
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean

        # Perform SVD
        U, Sigma, Vt = np.linalg.svd(X_centered, full_matrices=False)
        
        # Store the principal components
        self.components = Vt[:self.n_components]

    def transform(self, X):
        # Center the data
        X_centered = X - self.mean
        
        # Project data onto the principal components
        X_pca = np.dot(X_centered, self.components.T)
        
        return X_pca

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)
