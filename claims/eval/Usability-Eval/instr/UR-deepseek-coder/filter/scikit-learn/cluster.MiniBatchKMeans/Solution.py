from sklearn.cluster import MiniBatchKMeans
import numpy as np

# Example data
data = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

# Initialize MiniBatchKMeans
kmeans = MiniBatchKMeans(n_clusters=2, batch_size=4, random_state=0)

# Fit the model
kmeans.fit(data)

# Predict the cluster labels for the data
labels = kmeans.predict(data)

# Print the cluster centers and labels
print("Cluster Centers:", kmeans.cluster_centers_)
print("Labels:", labels)
