
import numpy as np
from sklearn.cluster import AgglomerativeClustering

# Load sample dataset
X = np.array([[1, 2], [3, 4], [5, 6]])

# Perform agglomerative clustering using linkage distance
ac = AgglomerativeClustering(linkage="ward", n_clusters=2)
y_pred = ac.fit_predict(X)
