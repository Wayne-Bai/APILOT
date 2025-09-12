import numpy as np
from sklearn.decomposition import NMF

# Example matrix X (data matrix)
X = np.array([[1, 2], 
              [3, 4]])

# Initializing the NMF model with 2 components
model = NMF(n_components=2, init='random', random_state=0)

# Factorize matrix X into W and H
W = model.fit_transform(X)
H = model.components_

print("Matrix W (basis):")
print(W)
print("Matrix H (coefficients):")
print(H)
print("Reconstruction (approximation of X):")
print(np.dot(W, H))
