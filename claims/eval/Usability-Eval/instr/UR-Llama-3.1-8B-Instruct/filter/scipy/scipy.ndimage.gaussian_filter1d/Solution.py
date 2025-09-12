import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Define the Gaussian filter parameters
sigma = 1.0  # Standard deviation of the Gaussian filter
order = 10  # Order of the filter (sigma is calculated from this value)

# Calculate the sigma value from the order
# The filter length is approximately 2*sigma+1
sigma = (np.arange(order) - order // 2) / (2 * np.sqrt(2 * np.log(2))) * sigma

# Create the Gaussian filter kernel
kernel = np.exp(-np.square(np.arange(-order // 2, order // 2 + 1)) / (2 * np.square(sigma)))
kernel /= np.sum(kernel)  # Normalize the kernel

# Pad the kernel to ensure it's symmetric
kernel = signal.convolve(kernel, kernel, mode='full')[:order + 1]
kernel /= np.max(kernel)  # Normalize the kernel

# Create a sample 1D signal
t = np.linspace(-10, 10, 1000)
signal_in = np.sin(t) + 0.5 * np.sin(3 * t) + np.random.normal(0, 0.1, 1000)

# Apply the Gaussian filter to the signal
filtered_signal = signal.convolve(signal_in, kernel, mode='same')

# Plot the original and filtered signals
plt.plot(t, signal_in, label='Original Signal')
plt.plot(t, filtered_signal, label='Filtered Signal')
plt.legend()
plt.show()
