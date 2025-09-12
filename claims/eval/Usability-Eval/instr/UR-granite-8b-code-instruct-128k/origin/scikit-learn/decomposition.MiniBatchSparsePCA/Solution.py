from sklearn.decomposition import SparsePCA

# Assume X is your data matrix
sparsed_components = SparsePCA(n_components=10, alpha=0.1).fit_transform(X)
