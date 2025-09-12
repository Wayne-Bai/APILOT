from sklearn.decomposition import NMF
import numpy as np

# Let's assume X is your non-negative matrix
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create an NMF instance: model
model = NMF(n_components=2)

# Fit the model to X
W = model.fit_transform(X)

# components_ is the matrix H
H = model.components_
