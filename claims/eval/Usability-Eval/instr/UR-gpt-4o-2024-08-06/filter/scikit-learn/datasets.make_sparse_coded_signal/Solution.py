import numpy as np
from sklearn.decomposition import SparseCoder
from sklearn.decomposition import DictionaryLearning

# Define a dictionary with random elements
n_components = 6
n_features = 20

# Generate a random dictionary
np.random.seed(0)
D = np.random.rand(n_components, n_features)

# Generate a random sparse code
code_size = 5
sparse_code = np.zeros(n_components)
nonzero_indices = np.random.choice(n_components, code_size, replace=False)
sparse_code[nonzero_indices] = np.random.rand(code_size)

# Create the signal as a combination of dictionary elements
signal = sparse_code @ D

# Verify by reconstructing the signal using SparseCoder
coder = SparseCoder(dictionary=D, transform_algorithm='lasso_lars', transform_n_nonzero_coefs=code_size)
recovered_code = coder.transform(signal.reshape(1, -1))

print("Original sparse code:", sparse_code)
print("Recovered sparse code:", recovered_code.flatten())
