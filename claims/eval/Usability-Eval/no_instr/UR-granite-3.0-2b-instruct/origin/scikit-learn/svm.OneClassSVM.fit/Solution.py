from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np

def detect_soft_boundary(X, n_components=2):
    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Perform PCA
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)

    # Calculate the reconstruction error
    reconstruction_error = np.mean(np.linalg.norm(X - X_pca, axis=1) ** 2)

    # Return the soft boundary
    return reconstruction_error
