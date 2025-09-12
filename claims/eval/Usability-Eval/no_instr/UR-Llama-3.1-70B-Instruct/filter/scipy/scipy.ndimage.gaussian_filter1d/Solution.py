import scipy.ndimage as ndi
import numpy as np
import matplotlib.pyplot as plt

# Generate a 1D noisy signal
np.random.seed(0)
signal = np.random.normal(0, 1, 100) + np.sin(np.linspace(0, 10, 100))

# Define the standard deviation of the Gaussian filter
sigma = 5

# Apply the 1-D Gaussian filter
filtered_signal = ndi.gaussian_filter1d(signal, sigma, mode='nearest')

# Plot the original and filtered signals
plt.figure(figsize=(12, 6))
plt.plot(signal, label='Original Signal')
plt.plot(filtered_signal, label=f'Filtered Signal (sigma={sigma})')
plt.legend()
plt.show()
