from sklearn.cluster import MiniBatchKMeans
import numpy as np
import matplotlib.pyplot as plt

# Sample data: 1000 random points in 2D, clustered around five centers
np.random.seed(42)
data = np.random.randn(1000, 2)

# Initializing MiniBatchKMeans
kmeans = MiniBatchKMeans(n_clusters=5, batch_size=100, random_state=42)

# Fitting the model to the data
kmeans.fit(data)

# Retrieving the cluster centers
centers = kmeans.cluster_centers_

# Predicting the cluster for each data point
labels = kmeans.predict(data)

# Plotting the data and the computed cluster centers
plt.scatter(data[:, 0], data[:, 1], c=labels, s=10, cmap='viridis', alpha=0.5)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')
plt.title("Mini-Batch K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
