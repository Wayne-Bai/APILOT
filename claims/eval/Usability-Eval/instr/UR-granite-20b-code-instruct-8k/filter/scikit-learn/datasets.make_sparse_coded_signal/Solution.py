
from sklearn.sparse.linalg import sparse_encode
import numpy as np

# Generate a signal
np.random.seed(42)
X = np.random.randn(10, 5)

# Generate a dictionary
D = np.random.randn(20, 10)

# Generate a signal as a sparse combination of dictionary elements
Y = sparse_encode(X, D, n_nonzero_coefs=3)

print(Y)
