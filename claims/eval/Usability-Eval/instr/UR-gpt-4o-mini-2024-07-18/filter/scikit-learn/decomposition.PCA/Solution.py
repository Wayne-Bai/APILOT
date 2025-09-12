import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load sample data
data = load_iris()
X = data.data

# Create PCA instance
pca = PCA(n_components=2)

# Fit the PCA model and transform the data
X_pca = pca.fit_transform(X)

# Output the transformed data
print(X_pca)
