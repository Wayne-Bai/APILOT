from sklearn.decomposition import SparsePCA

# Create a sparse PCA model with 2 components and L1 penalty of 0.1
sparse_pca = SparsePCA(n_components=2, alpha=0.1)

# Fit the model to the data
sparse_pca.fit(data)

# Transform the data to the new sparse PCA components
new_data = sparse_pca.transform(data)
