from sklearn.decomposition import NMF
from sklearn.datasets import make_multi_class_sparse

# Generate a sparse matrix
X, y = make_multi_class_sparse(n_samples=100, n_features=100, n_classes=5, random_state=42)

# Initialize the NMF model
nmf = NMF(n_components=5, random_state=42)

# Fit the model to the data
nmf.fit(X)

# Print the learned basis vectors
print("Basis vectors:")
print(nmf.components_)

# Print the learned coefficients
print("\nCoefficients:")
print(nmf.transform(X))
