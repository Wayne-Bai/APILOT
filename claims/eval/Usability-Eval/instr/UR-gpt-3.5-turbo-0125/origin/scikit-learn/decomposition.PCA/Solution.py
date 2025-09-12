
import numpy as np

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None

    def fit(self, X):
        # Centering the data by subtracting the mean
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean

        # Singular Value Decomposition (SVD)
        U, S, Vt = np.linalg.svd(X_centered)

        # Get the first n_components columns of U
        self.components = Vt[:self.n_components]

    def transform(self, X):
        # Centering the data
        X_centered = X - self.mean

        # Projecting the data into a lower-dimensional space
        X_new = np.dot(X_centered, self.components.T)

        return X_new

# Example usage:
# pca = PCA(n_components=2)
# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# pca.fit(data)
# transformed_data = pca.transform(data)
# print(transformed_data)
