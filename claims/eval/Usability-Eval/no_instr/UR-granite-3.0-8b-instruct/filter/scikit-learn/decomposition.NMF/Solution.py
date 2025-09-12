from sklearn.decomposition import NMF
import numpy as np

# Assuming X is your non-negative matrix
X = np.array([[1, 2, 0], [4, 5, 6]])

# Initialize the NMF model with the desired number of components
nmf = NMF(n_components=2, init='random', random_state=0)

# Fit the model to the data
W = nmf.fit_transform(X)
H = nmf.components_

print("W:\n", W)
print("H:\n", H)
