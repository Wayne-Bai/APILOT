from sklearn.cluster import MiniBatchKMeans

# create the MiniBatchKMeans model with desired parameters
model = MiniBatchKMeans(n_clusters=3, max_iter=100, batch_size=6)

# fit the model to your data
model.fit(X)
