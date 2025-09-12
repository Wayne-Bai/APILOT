from sklearn.cluster import AgglomerativeClustering

# create the AgglomerativeClustering object with specified parameters
cluster = AgglomerativeClustering(n_clusters=None, distance_threshold=0)

# fit the model with the input data
cluster.fit(X)
