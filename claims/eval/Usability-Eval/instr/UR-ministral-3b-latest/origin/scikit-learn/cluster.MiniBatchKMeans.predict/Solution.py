from sklearn.cluster import KMeans
import numpy as np

# Assume X is your data
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])

# Create a KMeans instance with 2 clusters
kmeans = KMeans(n_clusters=2, random_state=0)

# Fit the model to the data
kmeans.fit(X)

# Predict the cluster each sample belongs to
predictions = kmeans.predict(X)

print(predictions)  # Output will show the indices of the clusters each sample belongs to
