from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

# Generate sample data
X, _ = make_blobs(n_samples=100, centers=3, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply Agglomerative Clustering
clustering = AgglomerativeClustering(n_clusters=3)
clustering.fit(X_scaled)

# Print the cluster labels
print(clustering.labels_)
