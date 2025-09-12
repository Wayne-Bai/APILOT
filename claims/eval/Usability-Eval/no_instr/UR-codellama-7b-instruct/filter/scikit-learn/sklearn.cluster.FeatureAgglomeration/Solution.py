
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import numpy as np

# Generate some sample data
data = pd.DataFrame({'feature1': [1, 2, 3, 4], 'feature2': [5, 6, 7, 8]})

# Create a clusterer object with the appropriate parameters
clusterer = AgglomerativeClustering(n_clusters=2)

# Fit the clustering model to the data
clusterer.fit(data)

# Get the cluster labels for each feature
labels = clusterer.labels_

# Print the clusters
print(labels)
