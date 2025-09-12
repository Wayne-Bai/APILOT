from sklearn.feature_extraction import DictVectorizer
from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Example data
data = [
    {'feature1': 1, 'feature2': 0.5},
    {'feature1': 1, 'feature2': 0.75},
    {'feature1': 0.5, 'feature2': 1},
    {'feature1': 0, 'feature2': 0.5},
]

# Convert the feature dictionary into an array
vectorizer = DictVectorizer(sparse=False)
X = vectorizer.fit_transform(data)

# Perform Agglomerative Clustering on features
agg_clustering = AgglomerativeClustering(n_clusters=2)
agg_clustering.fit(X)

# Output the labels assigned to each sample
print(f"Cluster labels: {agg_clustering.labels_}")
