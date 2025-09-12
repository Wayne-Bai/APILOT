
from sklearn.decomposition import PCA
import numpy as np

# Load your dataset
X = ... # replace with your data

# Perform linear dimensionality reduction using PCA
pca = PCA(n_components=3)
pca.fit(X)
X_reduced = pca.transform(X)

# Inverse the transformation and return a vector of size n_features
X_original = pca.inverse_transform(X_reduced)
print("Original data:", X_original)
