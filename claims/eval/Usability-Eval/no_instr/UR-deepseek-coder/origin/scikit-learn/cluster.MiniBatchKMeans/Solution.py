from sklearn.cluster import MiniBatchKMeans
import numpy as np

# Example data
data = np.random.rand(100, 2)  # 100 samples with 2 features each

# Initialize MiniBatchKMeans
kmeans = MiniBatchKMeans(n_clusters=3, batch_size=20, random_state=0)

# Fit the model
kmeans.fit(data)

# Predict the cluster labels for the data
labels = kmeans.predict(data)

# Print the cluster centers and labels
print("Cluster Centers:", kmeans.cluster_centers_)
print("Labels:", labels)
