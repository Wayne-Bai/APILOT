# Import required libraries
from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import load_iris
import numpy as np

# Load the iris dataset
data = load_iris()
X = data.data
y = data.target

# Create a MiniBatchKMeans object with k=3 (as there are 3 clusters)
kmeans = MiniBatchKMeans(n_clusters=3, random_state=0, batch_size=6)

# Fit model on data
kmeans.fit(X)

# Get cluster assignments for each data point
labels = kmeans.labels_

#Print the labels
print(labels)
