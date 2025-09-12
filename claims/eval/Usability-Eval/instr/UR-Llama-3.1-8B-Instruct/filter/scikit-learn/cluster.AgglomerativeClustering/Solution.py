# Import required libraries
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Generate sample data
np.random.seed(0)
X = np.random.rand(10, 2)  # 10 samples with 2 features

# Create Agglomerative Clustering model
# with the specified number of clusters
model = AgglomerativeClustering(n_clusters=3, affinity='euclidean',
                                linkage='ward')

# Fit the model to the data
model.fit(X)

# Predict the clusters for the data
labels = model.labels_

# Print the predicted labels for each sample
print("Cluster Labels:")
print(labels)

# Draw the sample data
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.title("Agglomerative Clustering")
plt.show()

# Draw the dendrogram to visualize the hierarchical clustering
Z = linkage(X, method='ward')
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title("Dendrogram of Hierarchical Clustering")
plt.show()
