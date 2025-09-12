from sklearn.cluster import KMeans

# Assume that we have a dataset X and the number of clusters k
k = 3  # for example

# create a KMeans instance with k clusters
kmeans = KMeans(n_clusters=k)

# fit the model to the data
kmeans.fit(X)

# predict the closest cluster each sample in X belongs to
labels = kmeans.predict(X)
