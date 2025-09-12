
from sklearn.decomposition import SparsePCA

# Create an instance of SparsePCA with desired parameters
sparse_pca = SparsePCA(n_components=5, alpha=0.1)

# Fit the SparsePCA model to the data
sparse_pca.fit(X)

# Transform the data to the sparse components
sparse_components = sparse_pca.transform(X)
