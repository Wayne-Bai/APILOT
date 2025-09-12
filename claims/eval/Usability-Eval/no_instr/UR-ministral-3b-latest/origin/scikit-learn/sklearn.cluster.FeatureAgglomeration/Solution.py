# Import the necessary libraries
from sklearn.cluster import AgglomerativeClustering

# Create an instance of the AgglomerativeClustering class
agglomerative = AgglomerativeClustering(n_clusters=2)  # Specify the number of clusters you want

# Example data
X = [[1, 2], [1, 4], [1, 0], [10, 2], [10, 1], [10, 3]]

# Fit the model to the data
agglomerative.fit(X)

# Get the cluster labels
labels = agglomerative.labels_

print("Cluster labels for each observation:", labels)
