from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Generate sample data
X = np.random.rand(100, 10)

# Perform agglomerative clustering with linkage distance
clusters = AgglomerativeClustering(n_clusters=5, linkage='ward').fit_predict(X)

# Print the predicted clusters
print(clusters)
