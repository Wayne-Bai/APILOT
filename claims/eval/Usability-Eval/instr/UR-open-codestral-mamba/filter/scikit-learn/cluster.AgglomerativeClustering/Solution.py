# import required libraries
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# create agglomerative clustering
agg = AgglomerativeClustering(n_clusters=4)

# fit and predict
clusters = agg.fit_predict(X)

# plot result
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.show()
