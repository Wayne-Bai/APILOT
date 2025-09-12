from sklearn.decomposition import SparsePCA
from sklearn.datasets import make_sparse_coded_signal

# Generate a sparse signal
X, _, _, _ = make_sparse_coded_signal(n_samples=1000, n_features=100, n_components=10, random_state=42)

# Apply SparsePCA to the signal
spca = SparsePCA(n_components=10, random_state=42)
X_sparse = spca.fit_transform(X)
