# Import required libraries
from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import make_blobs

# Create dummy data
X, y = make_blobs(n_samples=10000, centers=4, n_features=2, random_state=42)

# Define the MiniBatchKMeans clustering algorithm
kmeans = MiniBatchKMeans(n_clusters=4, random_state=0, batch_size=6)

# Train the algorithm on the dummy data
kmeans.fit(X)

# Predict clusters for new data
# For example, predicting clusters for first 10 points in X
predictions = kmeans.predict(X[:10])

# Print the predictions
print(predictions)
