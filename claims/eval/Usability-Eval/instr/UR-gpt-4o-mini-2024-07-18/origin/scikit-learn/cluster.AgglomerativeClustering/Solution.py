from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Sample data
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 0], [4, 4]])

# Applying Agglomerative Clustering
clustering = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
labels = clustering.fit_predict(X)

print("Cluster labels:", labels)
