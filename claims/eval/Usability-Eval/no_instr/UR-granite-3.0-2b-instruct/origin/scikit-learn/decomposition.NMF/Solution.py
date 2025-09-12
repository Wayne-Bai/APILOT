from sklearn.decomposition import NMF
from sklearn.datasets import load_iris
import numpy as np

# Load dataset
iris = load_iris()
X = iris.data

# Initialize NMF model
nmf = NMF(n_components=2, random_state=42)

# Fit the model to the data
nmf.fit(X)

# Get the word-document matrix W and the per-document matrix H
W = nmf.components_
H = nmf.transform(X)

# Print the matrices
print("W:\n", W)
print("H:\n", H)
