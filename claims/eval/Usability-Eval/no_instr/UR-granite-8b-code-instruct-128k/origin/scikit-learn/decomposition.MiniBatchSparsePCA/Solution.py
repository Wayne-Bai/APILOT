from sklearn.decomposition import SparsePCA

# Create a SparsePCA object with alpha=1 and n_components=2
sparse_pca = SparsePCA(n_components=2, alpha=1)

# Fit the model to the data
sparse_pca.fit(X)

# Transform the data using the sparse components
sparse_code = sparse_pca.transform(X)

# Inverse transform the data using the sparse components
reconstructed_data = sparse_pca.inverse_transform(sparse_code)
