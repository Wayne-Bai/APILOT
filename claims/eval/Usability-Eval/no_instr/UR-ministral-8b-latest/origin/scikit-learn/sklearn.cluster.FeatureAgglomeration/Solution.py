import numpy as np
from sklearn.cluster import AgglomerativeClustering

# Sample data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# Instantiate the AgglomerativeClustering model
clustering = AgglomerativeClustering(n_clusters=2)

# Fit the model
clustering.fit_predict(X)
