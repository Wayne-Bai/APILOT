import numpy as np
import networkx as nx
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import SpectralEmbedding

# Create a sample graph
G = nx.erdos_renyi_graph(n=10, p=0.5)

# Compute the normalized Laplacian
L = nx.normalized_laplacian_matrix(G).A  # Converting sparse matrix to dense

# Perform spectral embedding to project the normalized Laplacian
n_components = 2  # Number of dimensions for projection
embedding = SpectralEmbedding(n_components=n_components, affinity='precomputed', random_state=42)
X_embedded = embedding.fit_transform(L)

# Normalize the embedded data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_embedded)

# Apply KMeans clustering
n_clusters = 2  # Specify the number of clusters
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Output the cluster labels
print("Cluster labels:", clusters)
