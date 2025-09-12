
from sklearn.decomposition import PCA
import numpy as np

# Generate sample data
data = np.random.rand(100, 10)

# Perform Principal Component Analysis (PCA) using SVD
pca = PCA(n_components=2)
pca_results = pca.fit_transform(data)

# Print the resulting principal components
print("Principal Components:")
print(pca_results[:, 0])
print(pca_results[:, 1])
