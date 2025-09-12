
import numpy as np
from sklearn.decomposition import NMF

# Create a sample non-negative matrix X
X = np.array([[1, 0], [3, 4], [5, 6]])

# Perform NMF on X
model = NMF(n_components=2)
W = model.fit_transform(X)
H = model.components_

# Print the resulting matrices
print("Matrix W:")
print(W)
print("\nMatrix H:")
print(H)
