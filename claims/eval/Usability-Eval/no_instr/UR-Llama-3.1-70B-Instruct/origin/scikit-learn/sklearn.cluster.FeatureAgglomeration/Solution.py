# Import necessary libraries from scikit-learn
from sklearn.cluster import FeatureAgglomeration
from sklearn.datasets import load_iris
import numpy as np

# Load the iris dataset
iris = load_iris()
X = iris.data

# Create a FeatureAgglomeration object with 3 clusters
agglo = FeatureAgglomeration(n_clusters=3)

# Fit the object to the data and transform the data
X_reduced = agglo.fit_transform(X)

# Print the original and reduced feature shapes
print("Original feature shape:", X.shape)
print("Reduced feature shape:", X_reduced.shape)

# Get the cluster labels for each feature
cluster_labels = agglo.labels_

# Print the cluster labels for each feature
print("Feature cluster labels:", cluster_labels)

# To understand which features are clustered together,
# we can use the children_ attribute of the FeatureAgglomeration object
children = agglo.children_

# Since FeatureAgglomeration object is not a tree, 
# we cannot directly use the children_ attribute like a tree.
# However, we can convert it into a format that can be used to create a dendrogram.

# Convert the children_ into a format that can be used to create a dendrogram
def convert_children_to_linkage_matrix(children):
    n_features = X.shape[1]
    linkage_matrix = np.zeros((n_features - 1, 4))
    for i in range(n_features - 1):
        linkage_matrix[i, 0] = children[i, 0]
        linkage_matrix[i, 1] = children[i, 1]
        linkage_matrix[i, 2] = agglo.distances_[i]
        linkage_matrix[i, 3] = 2
    return linkage_matrix

linkage_matrix = convert_children_to_linkage_matrix(children)

# Now we can use the linkage_matrix to create a dendrogram if needed
