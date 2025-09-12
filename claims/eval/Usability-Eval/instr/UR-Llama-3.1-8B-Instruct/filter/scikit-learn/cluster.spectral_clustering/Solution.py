# Import necessary libraries
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.feature_extraction.image import grid_to_graph
import networkx as nx
import matplotlib.pyplot as plt

# Define a function to calculate the normalized Laplacian
def normalized_laplacian(adjacency_matrix):
    degree_matrix = np.diag(np.sum(adjacency_matrix, axis=1))
    laplacian_matrix = degree_matrix - adjacency_matrix
    normalized_laplacian_matrix = laplacian_matrix / degree_matrix
    return normalized_laplacian_matrix

# Create an example adjacency matrix (you can replace this with your own data)
adjacency_matrix = np.array([[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]])

# Calculate the normalized Laplacian
normalized_laplacian_matrix = normalized_laplacian(adjacency_matrix)

# Apply KPCA to the normalized Laplacian (equivalent to PCA on the Laplacian eigenmap)
pca = PCA(n_components=2)
eigenmap = pca.fit_transform(normalized_laplacian_matrix)

# Scale the eigenmap using StandardScaler
scaler = StandardScaler()
eigenmap_scaled = scaler.fit_transform(eigenmap)

# Create a grid graph with the same dimensions as the eigenmap
grid_graph = grid_to_graph(eigenmap_scaled.shape[0], eigenmap_scaled.shape[1])

# Apply KMeans clustering to the scaled eigenmap
kmeans = KMeans(n_clusters=5)
labels = kmeans.fit_predict(eigenmap_scaled)

# Plot the clusters
plt.figure(figsize=(10,8))
plt.scatter(eigenmap_scaled[:,0], eigenmap_scaled[:,1], c=labels)
plt.show()

# Plot the grid graph
G = nx.from_numpy_array(grid_graph)
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=12)
plt.show()
