from sklearn.cluster import MiniBatchKMeans

# Create a MiniBatchKMeans object with the desired number of clusters and batch size
mbk = MiniBatchKMeans(n_clusters=3, batch_size=1000)

# Fit the model to the data
mbk.fit(data)

# Get the cluster labels for each data point
labels = mbk.labels_

# Get the cluster centers
centers = mbk.cluster_centers_
