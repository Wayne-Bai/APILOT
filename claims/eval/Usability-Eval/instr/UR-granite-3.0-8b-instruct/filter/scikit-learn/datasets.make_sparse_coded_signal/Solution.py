import numpy as np
from sklearn.decomposition import MiniBatchSparsePCA

# Generate a random dictionary
np.random.seed(0)
n_samples, n_components, n_features = 100, 10, 1000
dictionary = np.random.randn(n_samples, n_components, n_features)

# Generate a sparse signal
alpha = 0.1  # sparsity level
n_sparse = int(alpha * n_features)
sparse_signal = np.zeros(n_features)
indices = np.random.choice(n_features, size=n_sparse, replace=False)
sparse_signal[indices] = np.random.randn(n_sparse)

# Generate the signal as a sparse combination of dictionary elements
signal = np.dot(dictionary, sparse_signal)

# Print the generated signal
print(signal)
