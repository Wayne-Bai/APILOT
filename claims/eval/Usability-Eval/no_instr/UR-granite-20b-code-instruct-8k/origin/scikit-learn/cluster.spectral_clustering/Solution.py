from sklearn.cluster import KMeans
from sklearn.datasets import make_circles
from sklearn.preprocessing import normalize
from sklearn.decomposition import KernelPCA

# Generate some example data
X, y = make_circles(n_samples=1000, factor=.3, noise=.05)

# Normalize the data
X_normalized = normalize(X, axis=1)

# Project the normalized data into a lower-dimensional space
pca = KernelPCA(kernel='rbf', gamma=10, random_state=0)
X_reduced = pca.fit_transform(X_normalized)

# Apply clustering to the lower-dimensional data
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X_reduced)

# Print the cluster labels
print(kmeans.labels_)
