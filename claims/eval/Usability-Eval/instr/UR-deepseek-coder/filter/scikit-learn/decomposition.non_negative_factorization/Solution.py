import numpy as np
from sklearn.decomposition import NMF

# Example non-negative matrix X
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Initialize NMF model with 2 components
model = NMF(n_components=2, init='random', random_state=0)

# Fit the model to the data
W = model.fit_transform(X)
H = model.components_

# Print the resulting matrices W and H
print("Matrix W:")
print(W)
print("Matrix H:")
print(H)
