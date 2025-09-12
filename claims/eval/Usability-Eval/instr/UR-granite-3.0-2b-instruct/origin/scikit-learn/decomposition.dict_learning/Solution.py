from sklearn.decomposition import NMF
from sklearn.datasets import make_multilabel_classification

# Generate a random binary matrix for demonstration
X, y = make_multilabel_classification(n_samples=100, n_features=20, n_classes=3, random_state=42)

# Convert the binary matrix to a sparse matrix
X = X.astype(int)
X = sp.csr_matrix(X)

# Initialize the NMF model with the desired number of factors
n_factors = 5
nmf = NMF(n_components=n_factors, random_state=42)

# Fit the model to the data
nmf.fit(X)

# Print the learned factors
print("Factors:")
print(nmf.components_)
