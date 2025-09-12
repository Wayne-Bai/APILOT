from sklearn.cluster import SpectralClustering
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA

# Generate a toy dataset with 4 clusters
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.4, random_state=0)

# Apply PCA to reduce dimensionality to 2
pca = PCA(n_components=2).fit(X)
X_pca = pca.transform(X)

# Apply spectral clustering to the projected dataset
clustering = SpectralClustering(n_clusters=4, affinity='nearest_neighbors', random_state=0).fit(X_pca)

# Print the labels
print(clustering.labels_)
