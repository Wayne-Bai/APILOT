from sklearn.cluster import KMeans
import numpy as np

# Assuming X is your input data
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])

# Initialize the KMeans model with 2 clusters
kmeans = KMeans(n_clusters=2, random_state=0)

# Fit the model to the data
kmeans.fit(X)

# Predict the closest cluster for each sample
predictions = kmeans.predict(X)

print(predictions)
