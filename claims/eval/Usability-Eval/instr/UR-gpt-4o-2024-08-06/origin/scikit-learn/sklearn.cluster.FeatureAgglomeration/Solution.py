import numpy as np
from sklearn.cluster import AgglomerativeClustering, FeatureAgglomeration
from sklearn.datasets import load_iris

# Load an example dataset
data = load_iris()
X = data.data

# Define the number of clusters/agglomerated features
n_clusters = 2

# Perform hierarchical/agglomerative clustering to merge similar features
# Note: Be sure to use properly functioning parts as AgglomerativeClustering.
clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
X_reduced = clustering.fit_transform(X.T).T

print("Original shape:", X.shape)
print("Reduced shape:", X_reduced.shape)
