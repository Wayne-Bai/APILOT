from sklearn.decomposition import NMF
from sklearn.datasets import make_sparse_coded_signal
import numpy as np

# Generate a random sparse coded signal
X = make_sparse_coded_signal(n_samples=100, n_features=50, n_components=3, random_state=0)

# Initialize the NMF model
nmf = NMF(n_components=2, random_state=0)

# Fit the model to the data
nmf.fit(X)

# Get the factorized matrices W and H
W = nmf.components_
H = nmf.transform(X)
