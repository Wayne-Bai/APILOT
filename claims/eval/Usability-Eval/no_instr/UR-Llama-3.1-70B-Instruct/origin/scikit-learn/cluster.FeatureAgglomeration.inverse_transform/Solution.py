import warnings
from sklearn.exceptions import FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)

from sklearn.decomposition import PCA
import numpy as np

class InversePCA:
    def __init__(self, n_components):
        self.pca = PCA(n_components=n_components)

    def fit(self, X):
        self.pca.fit(X)

    def transform(self, X):
        return self.pca.transform(X)

    def inverse_transform(self, X):
        return self.pca.inverse_transform(X)


if __name__ == "__main__":
    # Create a random dataset
    np.random.seed(0)
    X = np.random.rand(100, 5)

    # Create an instance of our inverse PCA
    ipca = InversePCA(n_components=3)
    
    # Fit the PCA to our dataset
    ipca.fit(X)

    # Transform the data into the new coordinate system
    X_new = ipca.transform(X)

    # Verify that the dimensions of the new dataset match what we expect
    print("New shape:", X_new.shape)

    # Invert the transformation
    X_inv = ipca.inverse_transform(X_new)

    # Verify that the inverted data has the same shape as the original
    print("Original shape after inversion:", X_inv.shape)
