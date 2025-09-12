
import numpy as np
from sklearn.cluster import KMeans

# Generate random data
X = np.random.rand(100, 3)

# Define the number of clusters (k)
k = 5

# Initialize k-means algorithm with k clusters
km = KMeans(n_clusters=k)

# Fit the data to the model
km.fit(X)

# Predict the cluster for each observation
preds = km.predict(X)

# Print the predicted clusters
print("Predicted clusters:")
for i in range(len(preds)):
    print("Cluster", i, "contains points:", X[preds == i])
