
from sklearn.cluster import KMeans
import numpy as np

# Generate some sample data
np.random.seed(0)
X = np.random.rand(10, 2)

# Create a KMeans object with 3 clusters
kmeans = KMeans(n_clusters=3)

# Fit the model to the data and predict the cluster for each sample
kmeans.fit(X)
predictions = kmeans.predict(X)

# Print the predicted clusters
print("Predicted clusters:", predictions)
