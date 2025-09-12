
from sklearn.decomposition import SparsePCA
import numpy as np

# Generate sample data
X = np.random.rand(100, 10)

# Perform Sparse Principal Components Analysis
sparse_pca = SparsePCA(n_components=5)
transformed_data = sparse_pca.fit_transform(X)

# Print the resulting sparse components
print(transformed_data)
