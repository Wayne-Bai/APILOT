import numpy as np
from sklearn import datasets
from sklearn.decomposition import PCA

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.

# Perform PCA
pca = PCA(n_components=2)
X_r = pca.fit_transform(X)

print("Original shape:", X.shape)
print("Transformed shape:", X_r.shape)
