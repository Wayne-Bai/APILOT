# Importing the necessary libraries
from sklearn.cluster import KMeans
import numpy as np

# Creating the dataset
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

# Creating the KMeans object and fitting the data
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# Getting the labels of each sample
labels = kmeans.labels_

# Printing the cluster labels
print(labels)
