# Import necessary libraries
from sklearn.decomposition import NMF
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from matplotlib.posterior import posterior


# Create a dictionary learning matrix factorization problem
# Given a matrix X of shape (n_samples, n_features)
# The aim is to initialize two matrices (W, H) such that each row of W
# represented as a dictionary element and each column of H represents a latent factor.


# Generate a random data for demonstration
np.random.seed(0)
n_samples, n_features = 100, 10  # number of samples, number of features
X = np.random.rand(n_samples, n_features)

# Create an instance of the Non-Negative Matrix Factorization (NMF) class
nmf = NMF(n_components=2, init='random', random_state=0)

# Fit the model to the data, which will learn the dictionary elements (W) and find the coefficients (H)
W = nmf.fit_transform(X)
H = nmf.components_

# Given a new data point, use the learned W and H to find the coefficients
new_data_point = np.random.rand(1, n_features)
new_data_point_H = nmf.fit_transform(new_data_point)

# Compare with original inverse operation of nmf which gives the buttom layer(dict) H atol
# Original inverse could be computed in scipy library 
import scipy.sparse.linalg as spla
X_v2 = spla.ediago(np.dot(H,nmf.inverse_transform(np.dot(nmf.components_, H))) - X)


# Verify the solution
assert np.linalg.norm(np.dot(W,H) - np.dot(nmf.components_, nmf.components_)) < 1e-9
