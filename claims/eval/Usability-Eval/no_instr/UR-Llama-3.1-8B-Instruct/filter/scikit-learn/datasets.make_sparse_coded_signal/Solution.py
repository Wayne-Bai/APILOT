# Import necessary libraries
from sklearn.decomposition import NMF
import numpy as np
import matplotlib.pyplot as plt

# Define a dictionary of atoms, which will be the basis vectors
atoms = np.array([
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0],
    [0, 0, 2],
])

# Create a signal as a sparse combination of dictionary elements
ground_truth_weights = [3, -1, 1, 0]
ground_truth_signal = np.dot(atoms, ground_truth_weights)

# Add some noise to the signal
noise_level = 0.05 * np.max(ground_truth_signal)
signal_with_noise = ground_truth_signal + noise_level * np.random.rand(*ground_truth_signal.shape)

# Reshape the signal to a column vector for NMF
signal_vec = signal_with_noise.ravel()

# Initialize NMF model
nmf = NMF(n_components=4, init='random', random_state=0)

# Fit the NMF model
nmf_utils = nmf.fit_transform(signal_vec.reshape(1,-1))

# Get the learned sparse coefficients
sparse_coefficients = nmf_utils[0]

# Display the sparse coefficients
print("Sparse Coefficients: ", sparse_coefficients)

# Display the original signal and the reconstructed signal
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.imshow(ground_truth_signal.reshape((1, -1)), aspect='auto', cmap='hot')
plt.title("Original Signal")
plt.subplot(1, 2, 2)
plt.imshow(nmf.transform(np.array([sparse_coefficients]).T).reshape((1, -1)), aspect='auto', cmap='hot')
plt.title("Reconstructed Signal")
plt.show()
