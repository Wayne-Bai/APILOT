from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Sample data: rows represent samples and columns represent features
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

# Initialize Agglomerative Clustering
agg_cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')

# Fit model 
cluster_labels = agg_cluster.fit_predict(X)

print("Cluster labels:", cluster_labels)
