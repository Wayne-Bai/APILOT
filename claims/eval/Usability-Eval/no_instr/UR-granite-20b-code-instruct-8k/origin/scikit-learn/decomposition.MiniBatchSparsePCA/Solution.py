from sklearn.decomposition import SparsePCA

# Create a SparsePCA object with specified number of components
sparse_pca = SparsePCA(n_components=3)

# Fit and transform the data
X_transformed = sparse_pca.fit_transform(X)
