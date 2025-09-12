import numpy as np
from sklearn.decomposition import NMF

# Generate a random non-negative matrix X
np.random.seed(0)
X = np.random.rand(10, 10)

# Perform NMF on X with 2 components
nmf = NMF(n_components=2, random_state=0, max_iter=500)
W = nmf.fit_transform(X)
H = nmf.components_

# Print the approximated matrix X
X_approx = np.dot(W, H)
print(X_approx)
