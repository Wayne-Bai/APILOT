import numpy as np
from sklearn.decomposition import NMF

# Example non-negative data matrix X
X = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Initialize NMF and specify the number of components
model = NMF(n_components=2, init='random', random_state=0)

# Fit the model to X and perform the matrix factorization
W = model.fit_transform(X)
H = model.components_

# Display the factorized matrices W and H
print("Matrix W (Features):")
print(W)
print("Matrix H (Components):")
print(H)
