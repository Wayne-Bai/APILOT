from sklearn.decomposition import NMF
import numpy as np

# example data
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])

# create an NMF instance
model = NMF(n_components=2, init='random', random_state=0)

# perform the NMF algorithm
W = model.fit_transform(X)
H = model.components_

# the product of W and H approximates the original matrix X
approx_X = np.dot(W,H)
