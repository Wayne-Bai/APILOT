import numpy as np
from scipy.ndimage import gaussian_filter1d

# Define the input signal
signal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Define the standard deviation for the Gaussian kernel
sigma = 1.5

# Apply the 1-D Gaussian filter
filtered_signal = gaussian_filter1d(signal, sigma)

print("Original Signal:", signal)
print("Filtered Signal:", filtered_signal)
