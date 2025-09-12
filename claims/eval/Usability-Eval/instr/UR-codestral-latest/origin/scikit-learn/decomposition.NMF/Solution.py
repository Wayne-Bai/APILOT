from sklearn.decomposition import NMF
import numpy as np

# Create a non-negative matrix
X = np.array(
    [[1, 1, 1],
    [2, 4, 1],
    [3, 2, 2]]
)

# Create an instance for NMF
nmf = NMF(n_components=2, init='random', random_state=0)

# Fit the model to the matrix X
W = nmf.fit_transform(X)

# Get the components
H = nmf.components_

print("W:\n", W)
print("H:\n", H)
