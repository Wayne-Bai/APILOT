
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
import numpy as np

def kmeans_laplacian_clustering(adjacency_matrix, n_clusters=8):
    # Compute the normalized Laplacian of the adjacency matrix
    lap = np.linalg.inv(np.eye(adjacency_matrix.shape[0]) - adjacency_matrix)
    # Project the Laplacian onto the best low-dimensional space using SVD
    svd = TruncatedSVD(n_components=2, n_iter=7, random_state=42)
    svd.fit(lap)
    lap_reduced = svd.transform(lap)
    # Apply k-means clustering to the projected Laplacian matrix
    km = KMeans(n_clusters=n_clusters, random_state=42)
    km.fit(lap_reduced)
    return km.labels_
