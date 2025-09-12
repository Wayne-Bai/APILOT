from sklearn.cluster import KMeans
import numpy as np

# Assume we have some data X
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])

# Assume we know we want to find 2 clusters
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# Predict the closest cluster each sample in X belongs to
labels = kmeans.predict(X)

print(labels)
