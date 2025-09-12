from sklearn.cluster import KMeans

# Assume X is your data
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
labels = kmeans.labels_
