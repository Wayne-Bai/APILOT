from sklearn.cluster import KMeans

# Assuming that we have already fit the KMeans model
# Here is an example to create and fit a KMeans model
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

# To predict the closest cluster for each sample in X
labels = kmeans.predict(X)
