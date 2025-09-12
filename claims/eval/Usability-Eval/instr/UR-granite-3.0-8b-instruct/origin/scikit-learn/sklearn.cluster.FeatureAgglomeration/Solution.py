from sklearn.cluster import AgglomerativeClustering

# Assuming X is your feature matrix
X = ...

# Initialize the AgglomerativeClustering model
model = AgglomerativeClustering(n_clusters=None, affinity='euclidean', linkage='ward')

# Fit the model to the data
model.fit(X)

# Get the cluster labels for each feature
cluster_labels = model.labels_

# Print the cluster labels
print(cluster_labels)
