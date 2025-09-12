from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Sample data
data = np.array([[1, 2], [1, 4], [1, 0],
                 [4, 2], [4, 4], [4, 0]])

# Create an Agglomerative Clustering model
model = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')

# Fit the model to the data
model.fit(data)

# Get the labels of the clusters
labels = model.labels_

print("Cluster labels:", labels)
