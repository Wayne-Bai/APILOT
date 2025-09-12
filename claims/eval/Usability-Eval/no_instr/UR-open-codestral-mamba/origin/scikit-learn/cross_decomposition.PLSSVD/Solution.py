from sklearn.decomposition import PCA

# Create a PCA object with n_components=1 to get the first principal component
# Set svd_solver="full" to indicate using the full SVD algorithm
pca = PCA(n_components=1, svd_solver="full")

# Assume X is your dataset
# X = <data>

# Fit the model to your data
# pca.fit(X)

# Now, you can use pca.singular_values_ to access the singular values of the SVD
