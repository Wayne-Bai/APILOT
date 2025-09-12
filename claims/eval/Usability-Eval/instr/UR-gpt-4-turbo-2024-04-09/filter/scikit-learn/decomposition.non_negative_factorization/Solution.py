import numpy as np
from sklearn.decomposition import NMF

# Example data matrix X (non-negative)
X = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Initializing NMF with desired number of components
nmf = NMF(n_components=2, init='random', random_state=42)

# Fit the model to X and transform the data
W = nmf.fit_transform(X)
H = nmf.components_

print("Matrix W (basis):")
print(W)
print("Matrix H (coefficients):")
print(H)
print("Reconstruction (approximation of X):")
print(np.dot(W, H))
