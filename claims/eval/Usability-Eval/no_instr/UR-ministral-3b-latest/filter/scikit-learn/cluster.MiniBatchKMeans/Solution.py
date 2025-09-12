from sklearn.cluster import MiniBatchKMeans

# Assuming X is your dataset
# X = ...

# Define the Mini-Batch K-Means algorithm
minibatch_kmeans = MiniBatchKMeans(n_clusters=3, batch_size=1000, random_state=0)

# Fit the model to the data
minibatch_kmeans.fit(X)

# Predict the clusters for the data
labels = minibatch_kmeans.predict(X)

# Output the learned centers (centroids)
centers = minibatch_kmeans.cluster_centers_
