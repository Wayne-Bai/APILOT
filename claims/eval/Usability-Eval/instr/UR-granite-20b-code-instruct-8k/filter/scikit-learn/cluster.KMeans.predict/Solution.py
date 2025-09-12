from sklearn.cluster import KMeans

# create data
X = [[ 1, 2],
 [ 4, 8],
 [16, 32],
 [ 2, 4],
 [ 8, 16],
 [32, 64]]

# create clusters
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# predict clusters
predictions = kmeans.predict(X)

# print predictions
print(predictions)
