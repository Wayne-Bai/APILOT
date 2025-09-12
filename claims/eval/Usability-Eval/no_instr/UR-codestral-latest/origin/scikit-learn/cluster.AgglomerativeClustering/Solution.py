from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Creating a sample dataset
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Creating an instance of AgglomerativeClustering
clustering = AgglomerativeClustering(n_clusters=4, linkage='ward')

# Fit model
clustering.fit(X)

# Plotting
plt.scatter(X[:, 0], X[:, 1], c=clustering.labels_, cmap='rainbow')
plt.show()
