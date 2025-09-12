from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Assume X is your data matrix
# Replace it with your actual data
X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# Create an instance of AgglomerativeClustering
clustering = AgglomerativeClustering(n_clusters=None, distance_threshold=0, compute_full_tree=True)

# Fit the model and get the labels
clustering.fit(X)
labels = clustering.labels_

print("Clusters:", labels)
