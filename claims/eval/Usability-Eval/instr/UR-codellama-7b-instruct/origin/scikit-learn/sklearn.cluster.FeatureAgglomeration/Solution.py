from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Generate some sample data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])

# Perform hierarchical clustering with AgglomerativeClustering
clusters = AgglomerativeClustering(n_clusters=2, linkage='ward').fit_predict(X)
print(clusters)
