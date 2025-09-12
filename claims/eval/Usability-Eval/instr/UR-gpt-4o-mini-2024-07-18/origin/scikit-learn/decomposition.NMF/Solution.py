import numpy as np
from sklearn.decomposition import NMF

# Sample non-negative matrix X
X = np.array([[3, 5, 2],
              [4, 0, 0],
              [1, 1, 0]])

# Specify the number of components (rank of the factorization)
n_components = 2

# Create a NMF model
nmf_model = NMF(n_components=n_components, init='random', random_state=0)

# Fit the model and transform the data
W = nmf_model.fit_transform(X)
H = nmf_model.components_

# Display the results
print("Original non-negative matrix (X):\n", X)
print("Factor matrix (W):\n", W)
print("Component matrix (H):\n", H)

# Check the approximation
approximation = np.dot(W, H)
print("Approximated matrix (W * H):\n", approximation)
