
import numpy as np
from sklearn.random_projection import SparseRandomProjection
# Generate a random dictionary
n_components = 100
n_features = 1000
dictionary = np.random.randn(n_components, n_features)
# Generate a random sparse signal
sparse_signal = np.zeros(n_features)
sparse_signal[np.random.choice(n_features, size=n_components, replace=False)] = 1
# Project the sparse signal onto the dictionary using sparse random projection
projection = SparseRandomProjection(n_components=n_components, random_state=0)
projected_signal = projection.fit_transform(sparse_signal.reshape(1, -1))
# Reconstruct the original signal from the projected signal
reconstructed_signal = np.dot(dictionary, projected_signal.T)
# Print the original and reconstructed signals
print("Original signal:", sparse_signal)
print("Reconstructed signal:", reconstructed_signal.flatten())
