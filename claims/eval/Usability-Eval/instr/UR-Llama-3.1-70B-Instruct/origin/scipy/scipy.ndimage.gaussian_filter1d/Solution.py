import scipy.ndimage as ndimage
import numpy as np
import matplotlib.pyplot as plt

# Define a 1-D signal
t = np.linspace(0, 1, 100)
signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t) + 0.2 * np.random.randn(len(t))

# Apply 1-D Gaussian filter
filtered_signal = ndimage.gaussian_filter1d(signal, sigma=1)

# Plot the original and filtered signals
plt.figure(figsize=(12, 6))
plt.plot(t, signal, label='Original Signal')
plt.plot(t, filtered_signal, label='Filtered Signal')
plt.legend()
plt.show()
