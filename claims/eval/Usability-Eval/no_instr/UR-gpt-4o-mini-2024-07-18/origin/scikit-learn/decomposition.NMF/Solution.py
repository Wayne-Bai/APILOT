import numpy as np
from sklearn.decomposition import NMF

# Create an example non-negative matrix X
X = np.array([[1, 2, 3],
              [0, 1, 0],
              [2, 0, 1]])

# Define the number of components (or factors)
n_components = 2

# Initialize NMF model
model = NMF(n_components=n_components, init='random', random_state=42)

# Fit the model and transform the matrix X into W and H
W = model.fit_transform(X)
H = model.components_

# Output the results
print("Matrix W (Basis vectors):")
print(W)
print("\nMatrix H (Coefficients):")
print(H)
print("\nReconstructed Matrix (W * H):")
print(np.dot(W, H))
