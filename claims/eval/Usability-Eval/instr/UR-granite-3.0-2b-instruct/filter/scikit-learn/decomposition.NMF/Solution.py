from sklearn.decomposition import NMF
from sklearn.datasets import make_sparse_coded_signal

# Generate a random sparse coded signal
X, _ = make_sparse_coded_signal(n_samples=1000, n_features=100, n_components=50, random_state=42)

# Perform NMF
nmf = NMF(n_components=50, init='nndsvd', random_state=42)
nmf.fit(X)

# Print the non-negative matrices W and H
print("W:\n", nmf.components_)
print("H:\n", nmf.transform(X))
