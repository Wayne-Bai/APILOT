
from numpy import linalg as LA
import numpy as np

def dictionary_learning(X, n_atoms, alpha, max_iter):
    D = np.random.rand(X.shape[0], n_atoms)
    for _ in range(max_iter):
        # Sparse coding step
        Z = np.dot(LA.pinv(D), X)
        
        # Dictionary update step
        for k in range(n_atoms):
            idx = np.arange(n_atoms) != k
            D[:, k] = 0
            R = X - np.dot(D, Z) + np.outer(D[:, k], Z[k, :])
            
            if LA.norm(R) > alpha:
                D[:, k] = (1/alpha) * R[:, k]
            else:
                D[:, k] = R[:, k]

    return D

# Usage example
from sklearn import datasets
data = datasets.load_digits()
X = data.data.T
n_atoms = 20
alpha = 0.1
max_iter = 100
dictionary = dictionary_learning(X, n_atoms, alpha, max_iter)
