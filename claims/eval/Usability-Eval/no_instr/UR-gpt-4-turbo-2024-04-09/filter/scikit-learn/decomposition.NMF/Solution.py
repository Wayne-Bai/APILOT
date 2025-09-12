import numpy as np
from sklearn.decomposition import NMF

# Sample data matrix X (non-negative elements)
X = np.array([[1, 2], [3, 4], [5, 6]])

# Initialize NMF model with number of components (topics)
model = NMF(n_components=2, init='random', random_state=42)

# Fit the model with matrix X
W = model.fit_transform(X)
H = model.components_

print("Matrix X:")
print(X)
print("Matrix W (basis):")
print(W)
print("Matrix H (coefficients):")
print(H)
print("Approximation of X by W*H:")
print(np.dot(W, H))
