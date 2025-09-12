from sklearn.decomposition import NMF
import numpy as np

# Let's assume we have a 4x6 matrix X
X = np.array([[1, 1], [1, 2], [2, 2], [1, 1]])

# We want to decompose X into the product of two non-negative matrices W and H
nmf = NMF(n_components=2)

# Separate matrix X into the dot product of non-negative factor matrices W and H
nmf.fit(X)
W = nmf.transform(X)
H = nmf.components_

print("Matrix W: \n", W)
print("Matrix H: \n", H)
