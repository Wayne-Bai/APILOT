from sklearn.cluster import KMeans

# Initialize the KMeans model
kmeans = KMeans(n_clusters=3) # adjust the number of clusters according to your data

# Fit the model to your data
kmeans.fit(X)

# Predict the closest cluster each sample in X belongs to
labels = kmeans.predict(X)
