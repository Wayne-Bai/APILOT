from sklearn.decomposition import PCA
import numpy as np

# Example data
data = np.array([[2.5, 2.4],
                 [0.5, 0.7],
                 [2.2, 2.9],
                 [1.9, 2.2],
                 [3.1, 3.0],
                 [2.3, 2.7],
                 [2, 1.6],
                 [1, 1.1],
                 [1.5, 1.6],
                 [1.1, 0.9]])

# Create a PCA object, here n_components specifies the number of principal components to compute
pca = PCA(n_components=2)

# Fit the model with data and apply the dimensionality reduction
principal_components = pca.fit_transform(data)

# Get the explained variance ratio
explained_variance_ratio = pca.explained_variance_ratio_

print("Principal Components:\n", principal_components)
print("Explained Variance Ratio:", explained_variance_ratio)
