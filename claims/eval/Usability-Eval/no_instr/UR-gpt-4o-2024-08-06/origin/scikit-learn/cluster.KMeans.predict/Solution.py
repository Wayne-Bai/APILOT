# Import necessary libraries
from sklearn.cluster import KMeans
import numpy as np

# Sample data
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

# Define the number of clusters
n_clusters = 2

# Create a KMeans instance with the desired number of clusters
kmeans = KMeans(n_clusters=n_clusters, random_state=42)

# Fit the model on the data
kmeans.fit(X)

# Predict the closest cluster each sample in X belongs to
predicted_clusters = kmeans.predict(X)

# Output the predicted clusters
print("Predicted clusters for each sample in X:")
print(predicted_clusters)
