from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import make_scatter
import numpy as np

# Generate random data
X, _ = make_scatter(n_samples=1000, random_state=42)

# Initialize MiniBatchDictionaryLearning with the desired number of features
dict_learning = MiniBatchDictionaryLearning(n_components=100, random_state=42)

# Fit the model to the data
dict_learning.fit(X)

# Get the learned dictionary
dictionary = dict_learning.components_

# Initialize MiniBatchKMeans with the desired number of clusters
kmeans = MiniBatchKMeans(n_clusters=10, random_state=42)

# Fit the model to the data using the learned dictionary as the transformer
kmeans.fit(X, dictionary)

# Get the cluster labels
labels = kmeans.labels_
