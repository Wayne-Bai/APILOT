from sklearn.cluster import AgglomerativeClustering

# create the clustering model
model = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')

# fit the model with the data
model.fit(X)

# get the cluster labels
labels = model.labels_

# get the cluster distances
distances = model.distances_
