from sklearn.decomposition import SparsePCA

# Assuming X is your data
X = ...  # Replace ... with your data

# Initialize the SparsePCA model with the desired number of components and alpha
sparse_pca = SparsePCA(n_components=5, alpha=0.1)

# Fit the model to the data
sparse_pca.fit(X)

# Get the sparse components
components = sparse_pca.components_

# Get the explained variance
explained_variance = sparse_pca.explained_variance_
