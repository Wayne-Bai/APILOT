from sklearn.cluster import MiniBatchKMeans

# Create a MiniBatchKMeans instance with desired parameters
kmeans = MiniBatchKMeans(n_clusters=3, random_state=0, batch_size=6)

# Fit the model to the data
kmeans.fit(X)

# Predict the cluster labels for the data
predictions = kmeans.predict(X)
