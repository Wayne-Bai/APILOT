from sklearn.decomposition import SparsePCA

# Create a SparsePCA instance with a specific alpha value for the sparsity control
alpha_value = 1.0
sparse_pca = SparsePCA(alpha=alpha_value)

# Example data: Replace this with your actual dataset
X = [[-1, -1, 0], [-2, -1, 0], [-3, -2, 0], [1, 1, 0], [2, 1, 0], [3, 2, 0]]

# Fit the model with X
sparse_pca.fit(X)

# Transform the data according to the sparse components
X_transformed = sparse_pca.transform(X)

# The components
components = sparse_pca.components_

# Print transformed data and components
print("Transformed Data:")
print(X_transformed)
print("Components:")
print(components)
