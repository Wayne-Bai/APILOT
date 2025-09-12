from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Generate sample data
X = np.random.rand(100, 2)

# Initialize Agglomerative Clustering
clustering = AgglomerativeClustering(n_clusters=3)

# Fit the model to the data
clustering.fit(X)

# Get the cluster labels
labels = clustering.labels_

print(labels)
