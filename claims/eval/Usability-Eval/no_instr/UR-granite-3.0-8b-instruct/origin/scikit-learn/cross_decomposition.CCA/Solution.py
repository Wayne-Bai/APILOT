from sklearn.cross_decomposition import CCA

# Assuming X and Y are your data matrices
X = ...  # Your first data matrix
Y = ...  # Your second data matrix

# Initialize the CCA model
cca = CCA(n_components=2)  # You can adjust the number of components as needed

# Fit the model to the data
cca.fit(X, Y)

# Get the canonical correlations
canonical_correlations = cca.transform(X, Y)

# Print the canonical correlations
print("Canonical Correlations:", canonical_correlations)
