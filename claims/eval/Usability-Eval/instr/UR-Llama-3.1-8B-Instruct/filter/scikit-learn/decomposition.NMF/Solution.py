# Import necessary libraries from scikit-learn
from sklearn.decomposition import NMF as NMFSklearn  # Using the latest version of NMF from scikit-learn
import numpy as np

# Generate a random 5x10 matrix as an example for matrix factorization
np.random.seed(0)
X = np.random.rand(5, 10)

# Create a new instance of NMF with 2 as the number of components
nmf = NMFSklearn(n_components=2, init='random', random_state=0)

# Fit the NMF model to the matrix X
W = nmf.fit_transform(X)
H = nmf.components_

# Print the results
print("Matrix W (components):")
print(W)
print("\nMatrix H (coefficients):")
print(H)
