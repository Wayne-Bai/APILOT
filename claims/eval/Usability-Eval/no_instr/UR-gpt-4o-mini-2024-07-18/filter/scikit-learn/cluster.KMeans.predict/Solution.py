from sklearn.cluster import KMeans
import numpy as np

# Sample data
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

# Initialize KMeans with the desired number of clusters
n_clusters = 2
kmeans = KMeans(n_clusters=n_clusters, random_state=0)

# Fit the model to the data
kmeans.fit(X)

# Predict the closest cluster each sample in X belongs to
predictions = kmeans.predict(X)

# Display the predictions
print(predictions)
