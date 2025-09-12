from sklearn.cluster import KMeans

# Assume X is the input data
# Fit the KMeans model to the data
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Predict the closest cluster for each sample in X
predictions = kmeans.predict(X)
