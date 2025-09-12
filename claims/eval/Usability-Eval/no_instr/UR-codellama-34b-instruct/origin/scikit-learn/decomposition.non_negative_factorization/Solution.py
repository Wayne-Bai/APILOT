
import numpy as np
from sklearn.decomposition import NMF

# Load the data
X = ... # a non-negative matrix

# Initialize the decomposition object
nmf = NMF(n_components=2, random_state=0)

# Factorize the matrix X
W, H = nmf.fit_transform(X)

# Print the results
print("W:", W)
print("H:", H)
