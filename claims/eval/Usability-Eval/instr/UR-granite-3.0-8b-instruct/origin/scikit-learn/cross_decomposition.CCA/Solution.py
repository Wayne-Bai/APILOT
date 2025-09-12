from sklearn.cross_decomposition import CCA

# Assuming X and Y are your data matrices
X = ...
Y = ...

# Initialize the CCA object
cca = CCA(n_components=2)

# Fit the model
cca.fit(X, Y)

# Get the canonical correlations
canonical_correlations = cca.canonical_correlations_

# Get the canonical variables
X_canonical, Y_canonical = cca.transform(X, Y)

# Print the canonical correlations
print("Canonical Correlations:", canonical_correlations)

# Print the canonical variables
print("X Canonical Variables:\n", X_canonical)
print("Y Canonical Variables:\n", Y_canonical)
