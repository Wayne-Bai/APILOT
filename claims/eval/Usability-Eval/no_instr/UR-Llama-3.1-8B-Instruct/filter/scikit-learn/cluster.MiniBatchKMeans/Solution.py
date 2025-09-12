# Import necessary libraries from scikit-learn
from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data with 3 clusters using make_blobs function
X, _ = make_blobs(n_samples=5000, n_features=2, centers=3, random_state=42)

# Split data into mini-batches of size 128
mini_batches = np.array_split(X, len(X) // 128 + (len(X) % 128!= 0))

# Initialize Mini-Batch K-Means model with 3 clusters
model = MiniBatchKMeans(n_clusters=3, batch_size=128, random_state=42)

# Fit the model to the data in mini-batches
for batch in mini_batches:
    model.partial_fit(batch)

# Predict cluster labels for all data points
y_pred = model.predict(X)

# Plot the data with cluster labels
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], marker='*', s=200, c='red')
plt.show()
