import numpy as np
from sklearn.decomposition import IncrementalPCA
from sklearn.preprocessing import StandardScaler

class SparsePCA:
    def __init__(self, n_components=None, alpha=0.5, batch_size=100):
        self.n_components = n_components
        self.alpha = alpha
        self.batch_size = batch_size
        self.pca = IncrementalPCA(n_components=self.n_components, batch_size=self.batch_size)

    def fit(self, X):
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
        self.pca.fit(X)
        self.components_ = np.abs(self.pca.components_) * self.alpha

    def transform(self, X):
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
        return self.pca.transform(X)

    def inverse_transform(self, X):
        return super().transform(X)

# Example usage:
# Initialize the SparsePCA object
sparse_pca = SparsePCA(n_components=10, alpha=0.01)

# Fit the model to the data
X = np.random.rand(100, 20)
sparse_pca.fit(X)

# Transform the data
X_transformed = sparse_pca.transform(X)
