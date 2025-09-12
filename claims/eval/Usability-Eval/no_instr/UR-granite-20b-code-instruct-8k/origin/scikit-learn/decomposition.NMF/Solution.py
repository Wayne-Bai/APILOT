from sklearn.decomposition import NMF
import numpy as np

# Assuming you have a non-negative matrix X
X = np.array([[1, 0, 3], [2, 1, 1], [0, 2, 2], [3, 2, 0]])

# Initialize the NMF model with k components
nmf = NMF(n_components=2, init='random', random_state=0)

# Fit the model to the data
W = nmf.fit_transform(X)
H = nmf.components_

print("Factorization:", W, H)
