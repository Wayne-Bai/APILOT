from sklearn.decomposition import NMF
from sklearn.datasets import make_sparse_coded_signal
from sklearn.preprocessing import StandardScaler
import numpy as np

# Generate a random sparse coded signal
X = make_sparse_coded_signal(n_samples=100, n_features=50, n_components=3, random_state=42)

# Standardize the matrix
X = StandardScaler().fit_transform(X)

# Apply NMF
nmf = NMF(n_components=2, random_state=42)
W, H = nmf.fit_transform(X), nmf.components_

# Print the factors
print("W:\n", W)
print("H:\n", H)
