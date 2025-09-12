from sklearn.decomposition import SparsePCA

def apply_sparse_pca(data, alpha=1.0, n_components=2):
    # Create the SparsePCA object
    spca = SparsePCA(n_components=n_components, alpha=alpha)

    # Fit the data
    spca.fit(data)

    # Transform the data
    data_transformed = spca.transform(data)

    return data_transformed
