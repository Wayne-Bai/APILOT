from sklearn.cluster import MiniBatchKMeans

# Example dataset
X = [[1, 2], [1, 4], [1, 0],
     [10, 2], [10, 4], [10, 0]]

# Initialize and fit MiniBatchKMeans
mbk = MiniBatchKMeans(n_clusters=2, batch_size=2, random_state=0)
mbk.fit(X)

# Predict clusters for each data point
labels = mbk.predict(X)

print(f"Cluster labels: {labels}")
