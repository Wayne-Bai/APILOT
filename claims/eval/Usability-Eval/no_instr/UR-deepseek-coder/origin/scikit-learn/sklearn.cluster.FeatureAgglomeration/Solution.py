import numpy as np
from sklearn.cluster import FeatureAgglomeration
from sklearn.datasets import make_blobs

# Generate a sample dataset
X, _ = make_blobs(n_samples=100, n_features=20, centers=3, random_state=42)

# Initialize the FeatureAgglomeration model
agglo = FeatureAgglomeration(n_clusters=10)

# Fit the model and transform the data
X_reduced = agglo.fit_transform(X)

# Print the shape of the reduced dataset
print("Shape of the reduced dataset:", X_reduced.shape)
