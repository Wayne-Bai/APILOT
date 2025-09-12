
from sklearn.cluster import KMeans
import pandas as pd

# Load the dataset
data = pd.read_csv('data.csv')

# Create a Mini-Batch K-Means model with k=5 clusters
kmeans = KMeans(n_clusters=5, batch_size=100)

# Fit the data to the model
kmeans.fit(data)

# Predict the cluster assignments for each data point
predictions = kmeans.predict(data)

# Print the cluster centroids
print(kmeans.cluster_centers_)
