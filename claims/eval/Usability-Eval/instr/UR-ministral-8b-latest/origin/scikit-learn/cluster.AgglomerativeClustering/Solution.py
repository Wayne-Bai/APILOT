from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Assuming you have some sample data 'data'
data = np.array([[1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0]])

# Initialize the AgglomerativeClustering model with linkage method and number of clusters
model = AgglomerativeClustering(n_clusters=2, linkage='ward')

# Fit the model to the data
model.fit(data)

# Get the clustering labels
labels = model.labels_

print("Cluster labels:", labels)
