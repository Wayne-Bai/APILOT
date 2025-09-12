from sklearn.decomposition import SparsePCA
# Initialize the SparsePCA model with a specified number of components and the L1 penalty coefficient
spca = SparsePCA(n_components=2, alpha=0.1)
# Fit the model to the data
spca.fit(X)
# Transform the data using the fitted model
X_transformed = spca.transform(X)
