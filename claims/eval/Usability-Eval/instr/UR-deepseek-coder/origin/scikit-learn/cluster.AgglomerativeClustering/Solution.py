import numpy as np
from sklearn.cluster import AgglomerativeClustering

# Sample data
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

# Initialize Agglomerative Clustering
clustering = AgglomerativeClustering(n_clusters=2, linkage='ward')

# Fit the model and predict clusters
labels = clustering.fit_predict(X)

# Output the cluster labels
print(labels)
