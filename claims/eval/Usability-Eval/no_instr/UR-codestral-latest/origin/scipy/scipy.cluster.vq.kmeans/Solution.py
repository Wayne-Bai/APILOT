from sklearn.cluster import KMeans
import numpy as np

# Let's assume this is your data
data = np.random.rand(100, 2)  # An array of 100 observations in 2 dimensions

# Define the number of clusters
n_clusters = 3

# Use sklearn's k-means function
kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(data)

# Get the cluster labels and the coordinates of the cluster centers
labels = kmeans.labels_
cluster_centers = kmeans.cluster_centers_

print("Cluster Labels: ", labels)
print("Cluster Centers: ", cluster_centers)
