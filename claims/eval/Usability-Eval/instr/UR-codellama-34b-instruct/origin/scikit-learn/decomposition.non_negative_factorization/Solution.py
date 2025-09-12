import numpy as np
from sklearn.decomposition import NMF

# Create a random non-negative matrix X
X = np.random.rand(10, 10)

# Initialize the NMF algorithm with the number of components k=2
nmf = NMF(n_components=2)

# Fit the model to the data
W = nmf.fit_transform(X)
H = nmf.components_

# Compute the approximation error
error = np.linalg.norm(X - W @ H) / np.linalg.norm(X)

print("Approximation error:", error)
