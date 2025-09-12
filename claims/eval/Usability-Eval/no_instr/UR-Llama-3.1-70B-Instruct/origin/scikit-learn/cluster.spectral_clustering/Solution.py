# Import necessary libraries
from sklearn.cluster import KMeans, SpectralClustering
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import normalize
from sklearn.utils import check_random_state
from sklearn.metrics.pairwise import rbf_kernel
import numpy as np
import matplotlib.pyplot as plt

# Generate a random dataset
random_state = check_random_state(0)
n_samples = 200
n_features = 2
X = random_state.rand(n_samples, n_features)

# Apply RBF kernel to the dataset
gamma = 1
K = rbf_kernel(X, gamma=gamma)

# Compute the normalized Laplacian
D = np.diag(1 / np.sqrt(np.sum(K, axis=1)))
L = np.eye(n_samples) - np.dot(D, np.dot(K, D))

# Compute the eigenvectors and eigenvalues
eig_vals, eig_vecs = np.linalg.eig(L)

# Sort the eigenvectors and eigenvalues in ascending order
idx = eig_vals.argsort()
eig_vals = eig_vals[idx]
eig_vecs = eig_vecs[:, idx]

# Select the top k eigenvectors
k = 5
eig_vecs_k = eig_vecs[:, 1:k + 1]

# Apply k-means clustering to the projected data
kmeans = KMeans(n_clusters=5, random_state=0)
kmeans.fit(eig_vecs_k)
labels_kmeans = kmeans.labels_

# Apply spectral clustering to the normalized Laplacian
spectral = SpectralClustering(n_clusters=5, random_state=0)
spectral.fit(L)
labels_spectral = spectral.labels_

# Print the silhouette scores
print("KMeans Silhouette Score:", silhouette_score(eig_vecs_k, labels_kmeans))
print("Spectral Clustering Silhouette Score:", silhouette_score(L, labels_spectral))

# Plot the clusters
plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.scatter(eig_vecs_k[:, 0], eig_vecs_k[:, 1], c=labels_kmeans, cmap='viridis')
plt.title("KMeans Clustering")

plt.subplot(122)
plt.scatter(eig_vecs_k[:, 0], eig_vecs_k[:, 1], c=labels_spectral, cmap='viridis')
plt.title("Spectral Clustering")

plt.show()
