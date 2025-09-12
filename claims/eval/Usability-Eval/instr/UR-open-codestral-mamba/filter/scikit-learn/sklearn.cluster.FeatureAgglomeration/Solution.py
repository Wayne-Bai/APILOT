from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Assuming we have some sample features
X = np.array([[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]])
clustering = AgglomerativeClustering().fit(X)
labels = clustering.labels_

print("Cluster Labels: ", labels)
